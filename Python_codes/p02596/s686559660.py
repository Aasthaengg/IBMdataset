# Respect
K = int(input())
ans = 0
rem = 0
for i in range(K):
    rem = (10*rem + 7)%K
    if rem == 0:
        print(ans+1)
        quit()
    ans += 1
print(-1)