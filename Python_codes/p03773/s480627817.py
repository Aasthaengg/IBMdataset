x=list(input().split())
a=int(x[0])
b=int(x[1])
time=a+b
if time>=24:
  time-=24
print(time)