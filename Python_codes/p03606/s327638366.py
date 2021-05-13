n=int(input())
box=[list(map(int,input().split())) for _ in range(n)]
sum=0
for i in range(n):
  sum+=box[i][-1]-box[i][0]+1
print(sum)
