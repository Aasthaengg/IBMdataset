n=int(input())
m=[]
t=[]
for i in range(n):
  a,b=input().split()
  m.append(a)
  t.append(int(b))
c=input()
d=m.index(c)
print(sum(t[d+1:]))