n=input()
  
s=range(1,14)
h=range(1,14)
c=range(1,14)
d=range(1,14)
   
for i in range(n):
   m, k=raw_input().split()
   if m == 'S':
      s[int(k)-1] = 0
   elif m == 'H':
      h[int(k)-1] = 0
   elif m == 'C':
      c[int(k)-1] = 0
   elif m == 'D':
      d[int(k)-1] = 0
  
for i in range(0, 13):
   if s[i] != 0:
      print 'S '+str(s[i])
  
for i in range(0, 13):
   if h[i] != 0:
      print 'H '+str(h[i])
  
for i in range(0, 13):
   if c[i] != 0:
      print 'C '+str(c[i])
  
for i in range(0, 13):
   if d[i] != 0:
      print 'D '+str(d[i])