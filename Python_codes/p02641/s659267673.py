X, N = map(int, input().split())
p = list(map(int, input().split()))

l = []

for i in range(-1, 102, 1):
    if i not in p:
        l.append(i)

ans = []

for i in l:
    ans.append(abs(X-i))

ind = ans.index(min(ans))

print(l[ind])
