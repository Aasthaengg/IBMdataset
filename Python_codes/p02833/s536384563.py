n = int(input())
if n%2 == 0:
    i = 1
    ans = 0
    while 2*pow(5,i) <= n:
        ans += n//(2*pow(5,i))
        i += 1
    print(ans)
else:
    print(0)