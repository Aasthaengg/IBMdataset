# coding:utf-8
n = int(input())
s = [int(input()) for _ in range(n)]
s.sort()
ans = sum(s)

if ans % 10 != 0:
    print(ans)
    exit()
else:
    for i in range(n):
        if s[i] % 10 != 0:
            ans -= s[i]
            if ans % 10 != 0:
                print(ans)
                exit()
print(0)
