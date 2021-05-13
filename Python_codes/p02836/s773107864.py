import copy

s=list(input())

s2 = copy.copy(s)

s2.reverse()

ans = 0

for i in range(len(s)//2):
    if s[i] != s2[i]:
        ans += 1
print(ans)