a, b, c = map(int, input().split())
if a%2 == 0 and a == b and c == b:
    print(-1)
else:
    ans = 0
    while a%2 == b%2 == c%2 ==0:
        ans += 1
        a,b,c=(b+c)/2,(c+a)/2,(a+b)/2
    print(ans)