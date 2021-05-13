n=int(input())
s=[0]*((2*(10**5))+1)
a=list(map(int,input().split()))

for i in a:
  s[i-1]+=1
for i in range(n):
  print(s[i])
