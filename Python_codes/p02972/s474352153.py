n =int(input())
A = list(map(int, input().split()))

ans = [0]*n
for i in reversed(range(n)):
    j = i+1
    b = 0
    while j <= n:
        b += ans[j-1]
        j += (i+1)
    if b%2 == A[i]:
        ans[i] = 0
    else:
        ans[i] = 1
print(sum(ans))
B = []
for i in range(len(ans)):
    if ans[i] != 0:
        B.append(i+1)
print(*B)