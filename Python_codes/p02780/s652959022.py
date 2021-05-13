n,k = map(int, input().split())
P = list(map(int, input().split()))
a = []
for p in P:
    a.append((1+p)/2)
ans = [sum(a[:k])]
for i in range(1,len(a)-(k-1)):
    ans.append(ans[-1]-a[i-1]+a[i+k-1])
print(max(ans))