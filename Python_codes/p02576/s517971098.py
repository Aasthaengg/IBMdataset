n,x,t = (int(x) for x in input().split())

mod = n%x
M = int(mod)
time = (n-M)/x
Time = int(time+1)
if M == 0:
  Time = int(time)
print(Time*t)