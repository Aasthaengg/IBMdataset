n=int(input())
s=[input() for _ in range(n)]
m=int(input())
t=[input() for _ in range(m)]

s1=set(s)
a=b=0
for ss in s1:
  a=s.count(ss)-t.count(ss)
  if a>b:
    b=a
print(b)