k = int(input())
aa = list(map(int, input().split()))[::-1]
b=t=2
for a in aa:
    b += (a-b%a)%a
    t -= t%a
    t += a-1
    if b > t:
        print(-1)
        exit()
print(b,t)