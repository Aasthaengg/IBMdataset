#k = int(input())
#s = input()
#a, b = map(int, input().split())
#s, t = map(str, input().split())
#l = list(map(int, input().split()))
#l = [list(map(int,input().split())) for i in range(n)]
#a = [list(input()) for _ in range(n)]
#a = [int(input()) for _ in range(n)]

n,m,x=map(int, input().split())
a = list(map(int, input().split()))

ans1 = 0
for i in range(x,n+2):
    if i in a:
        ans1 += 1
ans2 = 0
for i in range(x):
    if i in a:
        ans2 += 1


print(min(ans1, ans2))



