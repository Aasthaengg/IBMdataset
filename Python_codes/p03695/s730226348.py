#C - Colorful Leaderboard 

N = int(input())
A = list(map(int, input().split()))

n = 399
a, b, c, d, e, f, g, h, z = 0,0,0,0,0,0,0,0,0

for i in A:
    if i >= 1 and i <= n:
        a = 1
    elif i >= 400 and i <= n + 400:
        b = 1
    elif i >= 2*400 and i <= 2*400 + n:
        c = 1
    elif i >= 3*400 and i <= 3*400 + n:
        d = 1
    elif i >= 4*400 and i <= 4*400 + n:
        e = 1
    elif i >= 5*400 and i <= 5*400 + n:
        f = 1
    elif i >= 6*400 and i <= 6*400 + n:
        g = 1
    elif i >= 7*400 and i <= 7*400 + n:
        h = 1
    else:
        z += 1

min_num, max_num = 0, 0
        
min_num = a+b+c+d+e+f+g+h


max_num = min_num + z
min_num = max(1, min_num)

print(min_num,max_num)