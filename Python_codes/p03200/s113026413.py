s = input()
ans = 0
cnt = 0
for ind,si in enumerate(s):
    if(si=='W'):
        ans += ind
        cnt += 1

ans -= (cnt*(cnt-1))//2
print(ans)