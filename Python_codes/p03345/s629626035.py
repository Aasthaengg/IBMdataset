a,b,c,k = map(int, input().split())
cheak = 10**18
ans = 0
if k % 2 == 0:
    ans = a-b
else:
    ans = b-a
if ans > cheak:
    print("Unfair")
else:
    print(ans)


