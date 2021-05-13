s=input()
m=1000
for i in range(len(s)-2):
  x=int(s[i]+s[i+1]+s[i+2])
  m=min(m,abs(x-753))

print(m)