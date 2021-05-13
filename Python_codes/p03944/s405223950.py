#k = int(input())
#s = input()
#a, b = map(int, input().split())
#s, t = map(str, input().split())
#l = list(map(int, input().split()))
#l = [list(map(int,input().split())) for i in range(n)]

w,h,n = map(int, input().split())

s = []

for i in range(h):
    retsu = []
    for j in range(w):
        retsu.append(0)
    s.append(retsu)

for i in range(n):
    x,y,a = map(int, input().split())
    if (a == 1):
        for i in range(h):
            for j in range(x):
                s[i][j] = 1
    elif a == 2:
        for i in range(h):
            for j in range(x,w):
                s[i][j] = 1
    elif a == 3:
        for i in range(y):
            for j in range(w):
                s[i][j] = 1
    else:
        for i in range(y,h):
            for j in range(w):
                s[i][j] = 1

#print(s)

ans = 0

for i in range(h):
    for j in range(w):
        if s[i][j] == 0:
            ans += 1
print(ans)
