#k = int(input())
#s = input()
#a, b = map(int, input().split())
#s, t = map(str, input().split())
#l = list(map(int, input().split()))
#l = [list(map(int,input().split())) for i in range(n)]
#a = [list(input()) for _ in range(n)]

K = int(input())
ans = 0
for i in range(1, K+1):
    for j in range(i+1, K+1):
        if (i % 2 == 0 and j % 2 != 0):
            ans += 1
        elif (i % 2 != 0 and j % 2 == 0):
            ans += 1
print(ans)


