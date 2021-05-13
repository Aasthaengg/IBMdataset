#k = int(input())
#s = input()
#a, b = map(int, input().split())
#s, t = map(str, input().split())
#l = list(map(int, input().split()))
#l = [list(map(int,input().split())) for i in range(n)]
#a = [list(input()) for _ in range(n)]
#a = [int(input()) for _ in range(n)]

a,b,c = map(int, input().split())

d = min(a,b,c)

ans = 0
if d == a:
    ans = d + min(b,c)
elif d == b:
    ans = d + min(a,c)
else:
    ans = d + min(a,b)
print(ans)


