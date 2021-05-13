coin_500 = int(input()) + 1
coin_100 = int(input()) + 1
coin_50 = int(input()) + 1
total = int(input())

cnt = 0

for i in range(coin_500):
    for j in range(coin_100):
        for k in range(coin_50):
            if 500 * i + 100 * j + 50 * k == total:
                cnt +=1
                
print(cnt)