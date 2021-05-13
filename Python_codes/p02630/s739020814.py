MAX = 10**5
N = int(input())
A = list(map(int, input().split()))

numlist = [0] * (MAX+1)
for i in range(N):
  numlist[A[i]] += 1
sumA = sum(A)
  
Q = int(input())
for i in range(Q):
  b, c = map(int, input().split())
  bcount = numlist[b]
  numlist[b] = 0
  numlist[c] += bcount
  sumA = sumA - bcount*b + bcount*c
  print(sumA)