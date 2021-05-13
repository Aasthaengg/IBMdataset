N=int(input())
max_a=0
point=0
for _ in range(N):
  A,B=map(int,input().split())
  if max_a<A:
    max_a=A
    point=B
print(max_a+point)
