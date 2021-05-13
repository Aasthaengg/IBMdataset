def f(n):
    if n%2==0: return n//2
    else: return 3*n+1
s = int(input())
v = set()
cnt = 1
while s not in v:
    v.add(s)
    s = f(s)
    cnt += 1
print(cnt)