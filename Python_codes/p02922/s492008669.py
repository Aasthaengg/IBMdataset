a, b = map(int, input().split())

if b == 1:
    print(0)

else:
    ans = 0
    y = 0
    while y < b:
        ans+=1
        y = ans*(a-1)+1
    print(ans)