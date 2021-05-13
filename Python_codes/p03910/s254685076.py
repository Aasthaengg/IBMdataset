n = int(input())

def f(n):
    return ((1 + n) * n) // 2
 
s = 0
for x in range(1, n+1):
    if f(x) > n:
        s = f(x)
        break

dif = s - n

for ans in range(1, x+1):
    if ans != dif:
        print(ans)