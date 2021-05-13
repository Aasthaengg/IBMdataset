n = int(input())
a1 = list(map(int, input().split()))
a2 = list(map(int, input().split()))

ans = []
for i in range(n+1):
    if i == 0:
        ans.append(sum(a1))
    elif 1<=i<=n:
        ans.append(sum(a1[:i]) + sum(a2[i-1:]))
    elif i==n:
        ans.append(sum(a2))
print(max(ans))