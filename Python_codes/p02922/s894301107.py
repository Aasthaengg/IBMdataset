A,B = map(int,input().split())
if B == 1:
    print(0)
elif B <= A:
    print(1)
else:
    ans = 1+int((B-A)/(A-1))
    if (B-A)%(A-1):
        ans += 1
    print(ans)