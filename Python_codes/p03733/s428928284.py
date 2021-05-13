n,T = map(int,input().split())
t = list(map(int,input().split()))
ans = 0
time = 0

for i in t:
    if time <= i:
        ans += T
        time = i + T
    else:
        ans += T - (time-i)
        time += T -  (time-i)
print(ans)



    
