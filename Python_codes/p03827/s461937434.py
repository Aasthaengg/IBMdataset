input()
a=t=0
for c in input():
  t+=(c>'D')*2-1
  a=max(a,t)
print(a)