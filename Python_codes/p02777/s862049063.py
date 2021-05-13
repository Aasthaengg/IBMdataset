S,T=input().split()
s,t=list(map(int, input().split()))
U=input()
if U==S:
  print(s-1,t)
else:
  print(s,t-1)
