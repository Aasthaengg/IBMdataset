N = int(input())
D,X = map(int,input().split())
As = [int(input()) for i in range(N)]
c = 0
for a in As:
  c+= 1 + (D-1)//a
print(c+X)