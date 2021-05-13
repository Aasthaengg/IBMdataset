n = int(input())
v_list = list(map(int,input().split()))
c_list = list(map(int,input().split()))
ans = 0
for i in range(n):
    dum = v_list[i]-c_list[i]
    if dum > 0:
        ans += dum
print(ans)