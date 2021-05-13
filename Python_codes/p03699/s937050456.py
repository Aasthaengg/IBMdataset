N = int(input())
s = [int(input()) for _ in range(N)]
ans = sum(s)
if ans % 10:
    print(ans)
else:
    l = [n if n % 10 else 99999999 for n in s]
    l.sort()
    if l[0] == 99999999:
        print(0)
    else:
        print(ans - l[0])