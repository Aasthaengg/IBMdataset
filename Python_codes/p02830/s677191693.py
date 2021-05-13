n=int(input())
s,t=map(str,input().split())
l=""
for i in range(n):
  l+=s[i]
  l+=t[i]

print(l)