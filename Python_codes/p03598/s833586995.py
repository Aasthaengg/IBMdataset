N=int(input())
K=int(input())
x=[int(n) for n in input().split()]
move=0
for i in range(N):
  move=move+min(2*x[i],2*abs(K-x[i]))
print(move)