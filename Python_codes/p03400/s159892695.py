N = int(input())
D,X = [int(i) for i in input().split()]
A = sorted([int(input()) for i in range(N)])

buf = 0
for i in A:
  buf+=(D-1)//i+1
print(X+buf)