n = int(input())
a = list(map(int , input().split()))
ans = 0
for ai in a:
    for i in reversed(range(1, 30)):
        if ai % pow(2, i) == 0:
            ans += i
            break
print(ans )
