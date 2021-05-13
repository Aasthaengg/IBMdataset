#k = int(input())
#s = input()
#a, b = map(int, input().split())
#s, t = map(str, input().split())
#l = list(map(int, input().split()))
#l = [list(map(int,input().split())) for i in range(n)]
#a = [list(input()) for _ in range(n)]
#a = [int(input()) for _ in range(n)]

n = int(input())

def func(n):
    rtn = 0
    for i in range(1,n+1):
        if (n % i == 0):
            rtn += 1
    return rtn

ans = 0
for i in range(1, n+1,2):
    if 8 == func(i):
        ans+=1
print(ans)
