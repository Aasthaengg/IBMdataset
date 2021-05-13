from math import gcd

N = int(input())
A = list(map(int,input().split()))
 
flg = 0
l = [0]*(max(A)+1)
for i in A:
  l[i] += 1
a = gcd(A[0],A[1])
for i in range(2,N):
  a = gcd(a,A[i])
for i in range(2,max(A)+1):
  if sum(l[i::i]) > 1:
    flg = 1
    break



if a == 1 and flg == 0:
  print("pairwise coprime ")
elif a == 1 and flg == 1:
  print("setwise coprime")
else:
  print("not coprime")
