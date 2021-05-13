#k = int(input())
#s = input()
#a, b = map(int, input().split())
#s, t = map(str, input().split())
#l = list(map(int, input().split()))
#l = [list(map(int,input().split())) for i in range(n)]

a, b = map(int, input().split())

ans = 0

for i in range(2):
    if (a > b):
        ans += a
        a -= 1
    else:
        ans += b
        b -= 1
print(ans)

