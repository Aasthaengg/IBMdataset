n = int(input())
if n % 2 == 1:
    print(0)
else:
    ans = 0
    for i in range(0,25):
        ans += n//(10*5**i)
    print(ans)