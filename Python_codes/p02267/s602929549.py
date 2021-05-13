n = int(input())
s = list(map(int, input().split()))
q = int(input())
t = list(map(int, input().split()))

ans = 0
for j in t:
    s.append(j)
    i = 0
    while s[i] != j:
        i += 1
    if i >= n:
        pass
    else:
        ans += 1
print(ans)