#k = int(input())
#s = input()
#a, b = map(int, input().split())
#s, t = map(str, input().split())
#l = list(map(int, input().split()))
#l = [list(map(int,input().split())) for i in range(n)]
#a = [list(input()) for _ in range(n)]
#a = [int(input()) for _ in range(n)]

n = int(input())
a = list(map(int, input().split()))

def func(a):
    rtn = 0
    while a % 2 == 0:
        a //= 2
        rtn+=1
    return rtn

for i in range(n):
    a[i] = func(a[i])
print(min(a))

