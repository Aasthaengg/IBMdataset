n, m = list(map(int, input().split()))
if n % 2 == 0 and m > 1:
    ans = list(range(1, m*2+1))
    s = (len(ans)//2)//2
    for i in range(len(ans)//2):
        if i < s:
            print(ans[i], ans[-1-i]+1)
        else:
            print(ans[i], ans[-1-i])
else:
    ans = list(range(1, m*2+1))
    for i in range(len(ans)//2):
        print(ans[i], ans[-1-i])
