#k = int(input())
#s = input()
#a, b = map(int, input().split())
#s, t = map(str, input().split())
#l = list(map(int, input().split()))
#l = [list(map(int,input().split())) for i in range(n)]
#a = [list(input()) for _ in range(n)]
#a = [int(input()) for _ in range(n)]

a = int(input())
b = int(input())
c = int(input())
x = int(input())

l = []
for i in range(a+1):
    for j in range(b+1):
        for k in range(c+1):
            l.append([i,j,k])


ans = 0
for i in range(len(l)):
    temp = l[i][0]*500 + l[i][1]*100 + l[i][2]*50
    if (temp == x):
        ans += 1
print(ans)

