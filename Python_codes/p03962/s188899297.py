s=list(map(int,input().split()))
a=s[0]
b=s[1]
if s.count(a)==3:
    print(1)
elif s.count(a)==2:
    print(2)
elif s.count(b)==2:
    print(2)   
else:
  print(3)
