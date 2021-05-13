def f(a,b,c):
    mx = max(a,b,c)
    mn = min(a,b,c)
    if mx == b or mn == b:
        return False
    else:
        return True

n = int(input())
p = list(map(int,input().split()))
cnt = 0
for i in range(n-2):
    if f(p[i],p[i+1],p[i+2]):
        cnt += 1
print(cnt)