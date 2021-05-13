n = int(input())
t = [0] * n
a = [0] * n
for i in range(n):
    tt, aa = map(int, input().split())
    t[i], a[i] = tt, aa

if n == 1:
    print(t[0]+a[0])
else:
    for i in range(1, n):
        for j in range(max(t[i-1]//t[i], a[i-1]//a[i]), 10**18):
            if t[i]*j >= t[i-1] and a[i]*j >= a[i-1]:
                t[i], a[i] = t[i] * j, a[i] * j
                break
    print(t[n-1]+a[n-1])