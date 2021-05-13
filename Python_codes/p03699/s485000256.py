n = int(input())
s = []
for _ in range(n):
    s.append(int(input()))

if all((i % 10 == 0 for i in s)):
    print(0)
else:
    s.sort()
    ans = sum(s)
    if ans % 10 != 0:
        print(ans)
    else:
        for i in s:
            if i % 10 != 0:
                print(ans - i)
                exit()
