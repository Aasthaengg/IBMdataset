s = int(input())

def f(n):
    if n%2: return 3*n+1
    else: return n//2

A = {s}
for ans in range(2, 10**6+10):
    if f(s) in A:
        print(ans)
        break
    A.add(f(s))
    s = f(s)
