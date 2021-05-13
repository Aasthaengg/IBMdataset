N = int(input())
d = list(map(int,input().split()))
sd = sorted(d)
#Kとしてあり得る値は sd[N // 2 - 1] + 1 から d[N // 2] までの合計 d[N // 2] - d[N // 2 - 1] 個
print(sd[N//2]-sd[N//2-1])