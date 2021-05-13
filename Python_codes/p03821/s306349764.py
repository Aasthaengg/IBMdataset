N = int(input())
A, B = [], []
for i in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)
    
A.reverse()
B.reverse()
count = 0
for i in range(N):
    now = A[i] + count
    if now % B[i] == 0:
        pass
    elif now < B[i]:
        count += B[i] - now
    else:
        count += B[i] - (now % B[i])

print(count)