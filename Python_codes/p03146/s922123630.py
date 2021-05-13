def func(n):
    return 3*n + 1 if n % 2 != 0 else n//2 

s = int(input())
inf = 1000000
l = []
l.append(s)
for i in range(1, inf+1):
    ai = func(l[i-1])
    if ai in l:
        print(i+1)
        break
    else:
        l.append(ai)