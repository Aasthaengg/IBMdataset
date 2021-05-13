n = int(input())
s = input()
t = input()
ans = len(s) + len(t)
c= 0
for i in range(n):
    j = n-i
    if s[i:] == t[:j]:
        ans = len(s[i:]) + len(t[:i]) + c
        break
    else:
        c+=1
print(ans)