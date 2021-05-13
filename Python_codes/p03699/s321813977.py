n = int(input())
s = list(int(input()) for i in range(n))

s.sort()

ans = sum(s)

if ans % 10 != 0:
    print(ans)
    exit()
else:
    for x in s:
        if x % 10 != 0:
            ans -= x
            print(ans)
            exit()
print(0)