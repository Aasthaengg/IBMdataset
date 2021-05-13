import sys
def input():
  return sys.stdin.readline().rstrip()

N=int(input())
a=list(map(int,input().split()))

s=0
for i in range(N):
  s+=a[i]

print(s-N)
