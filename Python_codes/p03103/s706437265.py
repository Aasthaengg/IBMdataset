N, M = map(int, input().split())
pAc = [list(map(int, input().split())) for _ in range(N)]
pAc.sort()
count = 0
price = 0
for p,c in pAc:
    if count + c >= M:
        print(price+(M-count)*p)
        exit()
    count += c
    price += p*c


