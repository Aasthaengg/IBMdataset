#k = int(input())
#s = input()
#a, b = map(int, input().split())
#s, t = map(str, input().split())
#l = list(map(int, input().split()))
#l = [list(map(int,input().split())) for i in range(n)]
#a = [input() for _ in range(n)]

n = int(input())


def func(n):
    if n%2==0:
        return n//2
    else:
        return 3*n+1

a = [n]
for i in range(2, 1000001):
    n = func(n)
    if n in a:
        print(i)
        exit()
    else:
        a.append(n)






