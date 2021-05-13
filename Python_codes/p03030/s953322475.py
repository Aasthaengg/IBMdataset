#k = int(input())
#s = input()
#a, b = map(int, input().split())
#s, t = map(str, input().split())
#l = list(map(int, input().split()))
#l = [list(map(int,input().split())) for i in range(n)]

n = int(input())
a = []
for i in range(n):
    s, p = map(str, input().split())
    p = int(p)
    a.append((s,p,i+1))
# 要素[1]を逆ソート
a.sort(key=lambda x:x[1], reverse=True)
# 要素[0]を順ソート
a.sort(key=lambda x:x[0])

for i in range(n):
    print(a[i][2])
