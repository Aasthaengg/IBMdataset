n = int(input())
ls = [list(map(int,input().split())) for i in range(n)]
a = 0
for i in range(n):
    a += (ls[i][1]-ls[i][0]+1)
print(a)