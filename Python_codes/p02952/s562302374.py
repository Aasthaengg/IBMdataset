n = int(input())
N = str(n)
num = len(N)
ans = 0
if num == 1:
    ans += n
elif num == 2:
    ans += 9
elif num == 3:
    ans += 9
    ans += (n-100+1)
elif num == 4:
    ans += 9
    ans += 900
elif num == 5:
    ans += 909
    ans += (n-10000+1)
elif num == 6:
    ans += 90909
print(ans)