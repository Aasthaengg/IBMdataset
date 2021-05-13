n = int(input())
B = list(map(int, input().split()))
A = [B[0]]
for i in range(n-1):
    if i != n-2:
        a = min(B[i], B[i+1])
    else:
        a = B[i]
    A.append(a)
print(sum(A))
