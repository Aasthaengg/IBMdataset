import sys
stdin = sys.stdin

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
nn = lambda: list(stdin.readline().split())
ns = lambda: stdin.readline().rstrip()

a,b,c,d,e,f = na()

p = e*100/(100+e)
a*=100
b*=100
ans = [a,0,0]

h = f//a
for i in range(h+1):
    w = (f-a*i)//b
    for j in range(w+1):
        q = f-a*i-b*j
        v = q//c
        for k in range(v+1):
            u = (q-c*k)//d
            for l in range(u+1):
                if c*k+d*l+a*i+b*j == 0:
                    continue
                n = (c*k+d*l)*100/(c*k+d*l+a*i+b*j)
                if n <= p and ans[2] < n:
                    ans = [c*k+d*l+a*i+b*j,c*k+d*l,n]

print(ans[0],ans[1])