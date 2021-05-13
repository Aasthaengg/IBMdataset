n=int(input())
c0=0
c1=0
c2=0
c3=0
for i in range(n):
  s=str(input())
  if s=="AC":
    c0+=1
  elif s=="WA":
    c1+=1
  elif s=="TLE":
    c2+=1
  else:
    c3+=1
print("AC x"+" "+str(c0))
print("WA x"+" "+str(c1))
print("TLE x"+" "+str(c2))
print("RE x"+" "+str(c3))