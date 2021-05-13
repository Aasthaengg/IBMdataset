import sys

def input():
  return sys.stdin.readline()

N=int(input())
A=list(map(int,input().split()))
B=[0]*(10**5)
for a in A:
  B[a-1]+=1
s=sum(A)
Q=int(input())
for i in range(Q):
  b,c=map(int,input().split())
  bb,bc=B[b-1],B[c-1]
  B[c-1]+=bb
  B[b-1]=0
  s+=bb*c-bb*b
  print(s)