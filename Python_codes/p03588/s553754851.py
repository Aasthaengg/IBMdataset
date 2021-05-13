N=int(input())

minarg_A=0
min_B=float("inf")
for _ in range(N):
  A,B=map(int,input().split())
  if B<min_B:
    min_B=B
    minarg_A=A
#print(minarg_A,min_B)

print(minarg_A+min_B)