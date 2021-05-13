n = int(input())
s = [int(i) for i in input().split()]
q = int(input())
t = [int(i) for i in input().split()]
ans = 0
for i in range(q):
    for j in range(n):
        if t[i] == s[j]:
            ans += 1
            break
print(ans)
