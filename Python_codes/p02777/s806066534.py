s,t = input().split()
a,b = [int(a)for a in input().split()]
c = input()
if c==s:
  print(a-1,b)
elif c==t:
  print(a,b-1)  