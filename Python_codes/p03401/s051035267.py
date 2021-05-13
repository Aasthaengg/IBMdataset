n=int(input())
l=[0]+list(map(int,input().split()))+[0]
s=sum(abs(l[i+1]-l[i]) for i in range(n+1))
for i in range(n):
  a,b,c=l[i:i+3]
  print(s-abs(b-a)-abs(c-b)+abs(c-a))