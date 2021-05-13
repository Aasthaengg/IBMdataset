c=0
while 1:
 a=input()
 if a.isdigit():
  c+=[1,int(a)][c>0]
 else:
  if c!=0:print((s*2)[c%l-1:][:l])
  if'-'==a:break
  s=a;l=len(s);c=0