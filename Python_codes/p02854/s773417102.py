n = int(input())
a = list(map(int,input().split()))
nagasa = sum(a)
now = 0
for i in range(n):
    if now + a[i] < nagasa/2:
        now += a[i]
    elif now + a[i] == nagasa/2:
        print(0)
        exit()
    elif now + a[i] > nagasa/2:
        print(min(nagasa-2*now,2*(now+a[i])-nagasa))
        exit()