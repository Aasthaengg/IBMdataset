a=input()
b=input()
c=input()
d=input()
leastnum=0
if a>=b and c>=d:
  leastnum=b+d
elif a>=b and d>=c:
  leastnum=b+c
elif b>=a and c>=d:
  leastnum=a+d
elif b>=a and d>=c:
  leastnum=a+c
print leastnum