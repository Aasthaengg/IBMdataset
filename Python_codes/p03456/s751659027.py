#k = int(input())
#s = input()
#a, b = map(int, input().split())
#s, t = map(str, input().split())
#l = list(map(int, input().split()))
#l = [list(map(int,input().split())) for i in range(n)]
#a = [list(input()) for _ in range(n)]
#a = [int(input()) for _ in range(n)]

a,b = map(str, input().split())

temp = int(a + b)

ans = "No"
for i in range(1, temp+1):
    if temp % i == 0:
        if temp // i == i:
            ans = "Yes"
            break
print(ans)

