s=int(input())
c=0
if s - int(s/10)*10 ==2:
    c=c+1
s=int(int(s/10))
if s - int(s/10)*10 ==2:
    c=c+1
s=int(int(s/10))
if s - int(s/10)*10 ==2:
    c=c+1
s=int(int(s/10))
if s - int(s/10)*10 ==2:
    c=c+1
s=int(int(s/10))

print(c)