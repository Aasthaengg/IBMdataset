a,b,c,d,e,f=map(int,input().split())
sw=set()
for i in range(30//a+1):
  for j in range(30//b+1):
    w=a*i+b*j
    if 0<w*100<=f: sw|={w}
ss=set()
for i in range(3000//c+1):
  for j in range(3000//d+1):
    s=c*i+d*j
    if s<=f: ss|={s}
lt=[]
for w in sw:
  for s in ss:
    t=w*100+s
    if t<=f and s<=w*e: lt+=[(-s/w,t,s)]
lt.sort()
print(*lt[0][1:])