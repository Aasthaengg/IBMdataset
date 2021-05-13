n = int(input())
a = list(map(int, input().split()))

ans = []
if max(a) >= -min(a):
    ans.append([a.index(max(a))+1, 1])
    ans.append([a.index(max(a))+1, 1])
    for i in range(n-1):
        ans.append([i+1, i+2])
        ans.append([i+1, i+2])

else:
    ans.append([a.index(min(a))+1, n])
    ans.append([a.index(min(a))+1, n])
    for i in range(n-1):
        ans.append([n-i, n-i-1])
        ans.append([n-i, n-i-1])

print(len(ans))
for i in range(len(ans)):
    print(" ".join(map(str, ans[i])))
