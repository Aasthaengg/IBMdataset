n, m, k = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
a = 0
b = 0
a_time = 0
b_time = 0
max_read = 0

for i in range(m):
    if b_time + B[i] > k:
        break
    else:
        b_time += B[i]
else:
    i += 1
b = i
max_read = b

for i in range(n):
    if a_time + A[i] > k:
        break
    
    a_time += A[i]
    a += 1
    if a_time + b_time <= k:
        max_read = max(max_read, a + b)
        continue
    else:
        while(a_time + b_time > k):
            b -= 1
            if b < 0:
                break
            b_time -= B[b]
        max_read = max(max_read, a + b)

print(max_read)