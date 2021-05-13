def convert(s): 
  
    # initialization of string to "" 
    new = "" 
  
    # traverse in the string  
    for x in s: 
        new += x  
  
    # return string  
    return new 

h,w,a,b=map(int,input().split())
k=[]
for i in range(a):
  k.append('0')
for i in range(w-a):
  k.append('1')
k=convert(k)
t=[]
for i in range(a):
  t.append('1')
for i in range(w-a):
  t.append('0')
t=convert(t)
for i in range(b):
  print(k)
for i in range(h-b):
  print(t)