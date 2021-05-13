#k = int(input())
#s = input()
#a, b = map(int, input().split())
#s, t = map(str, input().split())
#l = list(map(int, input().split()))
#l = [list(map(int,input().split())) for i in range(n)]


n,x = map(int, input().split())
l = list(map(int, input().split()))

temp = []

temp.append(0)
last = 0
for i in range(n):
    temp.append(last+l[i])
    last += l[i]
ans = 0
for i in range(n+1):
    if temp[i] <= x:
        ans += 1
print(ans)


