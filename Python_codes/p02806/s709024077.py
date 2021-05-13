n = int(input())
lis = []
for i in range(n):
    a , b = input().split()
    lis.append([a,int(b)])

x = input()

ans = 0
p = 0
for i in range(n):
    if p == 0 and lis[i][0] == x:
        p = 1
    elif p == 1:
        ans += lis[i][1]
print(ans)