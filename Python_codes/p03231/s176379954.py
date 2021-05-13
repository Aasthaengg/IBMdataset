def f(a,b):
    if b:
        return f(b,a%b)
    return a
n,m=map(int,input().split())
s=input()
t=input()
a=f(n,m)
print(n//a*m if s[::n//a]==t[::m//a] else -1)
