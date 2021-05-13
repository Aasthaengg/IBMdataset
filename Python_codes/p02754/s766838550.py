n, a, b = map(int,input().split())
a_b = n//(a+b)*a
if n%(a+b) < a:
    print(a_b + n%(a+b))
else:
    print(a_b + a)