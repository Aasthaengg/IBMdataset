#k = int(input())
#s = input()
#a, b = map(int, input().split())
#s, t = map(str, input().split())
#l = list(map(int, input().split()))
#l = [list(map(int,input().split())) for i in range(n)]
#a = [list(input()) for _ in range(n)]
#a = [input() for _ in range(n)]

n = int(input())
t,a = map(int, input().split())
h = list(map(int, input().split()))

ans = []


for i in range(n):
    tmp = t-h[i]*0.006
    ans.append([i+1,abs(a-tmp)])

ans.sort(key=lambda x:x[1])
print(ans[0][0])






