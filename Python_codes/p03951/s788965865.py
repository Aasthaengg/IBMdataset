N = int(input())
s = input()
t = input()
l1 = len(s)
l2 = len(t)
ans = l1+l2
for i in range(1,min(l1,l2)+1):
    if s[l1-i:] == t[:i]:
        ans = l1+l2-i
print(ans)