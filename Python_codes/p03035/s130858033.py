#k = int(input())
#s = input()
#a, b = map(int, input().split())
#s, t = map(str, input().split())
#l = list(map(int, input().split()))
#l = [list(map(int,input().split())) for i in range(n)]

a, b = map(int, input().split())

ans = 0

if (a >= 13):
    ans = b
elif(a >= 6 and a <= 12):
    ans = b // 2
else:
    pass
print(ans)

