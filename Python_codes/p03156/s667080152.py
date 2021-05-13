N = int(input())
A,B = map(int,input().split())
P = list(map(int,input().split()))
n1 = 0
n2 = 0
n3 = 0
for i in P:
  if i <= A:
    n1 += 1
  elif i <= B:
    n2 += 1
  else:
    n3 += 1
print(min(min(n1,n2),n3))