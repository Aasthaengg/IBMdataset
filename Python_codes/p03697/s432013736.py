#k = int(input())
#s = input()
#a, b = map(int, input().split())
#s, t = map(str, input().split())
#l = list(map(int, input().split()))
#l = [list(map(int,input().split())) for i in range(n)]
#a = [list(input()) for _ in range(n)]


a,b = map(int, input().split())

ans = a + b
if (ans >= 10):
    print("error")
else:
    print(ans)


