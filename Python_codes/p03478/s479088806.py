#k = int(input())
#s = input()
#a, b = map(int, input().split())
#s, t = map(str, input().split())
#l = list(map(int, input().split()))
#l = [list(map(int,input().split())) for i in range(n)]
#a = [list(input()) for _ in range(n)]
#a = [int(input()) for _ in range(n)]

n,a,b = map(int, input().split())

def func(s):
    rtn = 0
    for i in s:
        rtn += int(i)
    return rtn

ans = [0]
for i in range(1,n+1):
    temp = func(str(i))
    if (temp >= a and temp <= b):
        ans.append(i)

print(sum(ans))




