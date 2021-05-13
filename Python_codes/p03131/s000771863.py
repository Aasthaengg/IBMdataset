k, a, b = map(int, input().split())
k += 1
cnt =  k - (a + 2)

if b - a > 2 and cnt >= 0:
    ans = b + (b - a)*(cnt//2) + cnt%2
else:
    ans = k

print(ans)