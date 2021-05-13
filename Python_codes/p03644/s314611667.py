#k = int(input())
#s = input()
#a, b = map(int, input().split())
#s, t = map(str, input().split())
#l = list(map(int, input().split()))
#l = [list(map(int,input().split())) for i in range(n)]
#a = [list(input()) for _ in range(n)]
#a = [int(input()) for _ in range(n)]


n = int(input())

ans = 0
totalNum = -1
for i in range(1,n+1):
    temp = i
    num = 0
    while True:
        if (temp % 2 != 0):
            break
        else:
            temp = temp // 2
            num+=1
    if (totalNum < num):
        totalNum = num
        ans = i
print(ans)


