N = int(input())
s = sorted([int(input()) for _ in range(N)])
ans = sum(s)
if ans % 10 != 0:
    print(ans)
else:
    for s_i in s:
        if s_i % 10 != 0:
            ans -= s_i
            print(ans)
            break
    else:
        print(0)
