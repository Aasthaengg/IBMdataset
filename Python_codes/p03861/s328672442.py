#k = int(input())
#s = input()
#a, b = map(int, input().split())
#s, t = map(str, input().split())
#l = list(map(int, input().split()))
#l = [list(map(int,input().split())) for i in range(n)]

a,b,x = map(int, input().split())


def function(n,x):
    if (n>=0):
        return n//x+1
    else:
        return 0

ans = function(b,x) - function(a-1,x)

print(ans)
