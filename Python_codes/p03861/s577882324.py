a, b,c = map(int, input().split())
one = a//c
two = b//c
if c==1 or a%c==0:
  two+=1
print(two-one)