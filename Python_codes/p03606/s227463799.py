N=int(input())
ct=0
for _ in range(N):
  l=list(map(int, input().split()))
  ct+=l[1]-l[0]+1
print(ct)