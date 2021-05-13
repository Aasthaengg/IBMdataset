i,j=map(int,input().split())
matrix=[list(map(int,input().split())) for _ in range(i)]
vector=[int(input()) for _ in range(j)]
for x in range(i):
    print(sum([v * m for v,m in zip(vector,matrix[x])]))