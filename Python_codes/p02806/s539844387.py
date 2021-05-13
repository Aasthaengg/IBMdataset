n = int(input())
s = [0]*n
t = [0]*n
for i in range(n):
    s[i],t[i] = map(str,input().split())
    t[i] = int(t[i])
x = input()
a = s.index(x)
ans = sum(t[a+1:])
print(ans)