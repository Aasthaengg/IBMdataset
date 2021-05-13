#k = int(input())
#s = input()
#a, b = map(int, input().split())
#s, t = map(str, input().split())
#l = list(map(int, input().split()))
#l = [list(map(int,input().split())) for i in range(n)]
#a = [list(input()) for _ in range(n)]


a,b,c = map(int, input().split())

ans = "NO"
for i in range(1, b+1):
    if (a*i % b == c):
        ans = "YES"
        break
print(ans)

