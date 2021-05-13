x,y,a,b,c=map(int,input().split())
p=list(reversed(sorted(map(int,input().split()))))
q=list(reversed(sorted(map(int,input().split()))))
r=list(reversed(sorted(map(int,input().split()))))
p.append(2**100)
q.append(2**100)
r.append(-2**100)
s=sum(p[:x])+sum(q[:y])
t=0
while True:
  f=p[x-1]<q[y-1]
  m=p[x-1] if f else q[y-1]
  if m<r[t]:
    if f:
      x-=1
      s+=r[t]-p[x]
      t+=1
    else:
      y-=1
      s+=r[t]-q[y]
      t+=1
  else:
    break
print(s)
      
