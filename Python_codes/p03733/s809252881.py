N,T = map(int,input().split())
t = list(map(int,input().split()))
time = t[0]
ans = T
for i in t[1:]:
    if i - time < T:
        ans += i - time
    else :
        ans += T
    time = i
print(ans)