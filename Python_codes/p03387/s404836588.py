a, b, c = sorted(map(int, input().split()))
a += (c-b)
ans = (c-b)
if (c-a)%2==0:
    print(ans+(c-a)//2)
else:
    print(ans+(c-a)//2+2)
