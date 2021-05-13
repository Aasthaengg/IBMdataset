n = int(input())
ls = list(map(int,input().split()))
ls.sort()
if n % 2 == 0:
    if ls[::2] == ls[1::2] and ls[::2] == [e for e in range(n) if e % 2 != 0]:
        print(2**(int(n/2))%(10**9+7))
    else:
        print(0)
else:
    if ls[1::2] == ls[2::2] and ls[::2] ==  [e for e in range(n) if e % 2 == 0]:
        print(2**(int(n/2))%(10**9+7))
    else:
        print(0)