n, m, k = map(int, input().split())
a = list(map(int, input().split())) 
b = list(map(int, input().split())) 


sum_a = [0]
for i in range(n):
    sum_a.append(sum_a[i] + a[i])

sum_b = [0]
for i in range(m):
    sum_b.append(sum_b[i] + b[i])


a_i = 0
b_i = 0
for i in range(n+1):
    if sum_a[i] > k:
        break
    else:
        a_i = i

for i in range(m+1):
    if sum_a[a_i] + sum_b[i] > k:
        break
    else:
        b_i = i


ans = a_i + b_i
for i in range(a_i, -1, -1):
    for j in range(b_i, m+1):
        if sum_a[i] + sum_b[j] > k:
            b_i = j - 1
            break
        else:
            ans = max(ans, i+j)

print(ans)
