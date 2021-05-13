#k = int(input())
#s = input()
#a, b = map(int, input().split())
#s, t = map(str, input().split())
#l = list(map(int, input().split()))
#l = [list(map(int,input().split())) for i in range(n)]
#a = [input() for _ in range(n)]

n,m = map(int, input().split())
k = [list(map(int,input().split())) for i in range(n)]

ans = [0]*m

for i in range(n):
    for j in range(1, k[i][0]+1):
        #print(k[i][j] -1)
        ans[ k[i][j] -1] += 1

#print(ans)
print(ans.count(n))




