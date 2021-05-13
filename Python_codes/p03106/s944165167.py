A,B,K = list(map(int,input().split()))
count = 0
for i in range(100, 0, -1):
    if A % i == 0 and B % i == 0:
        count += 1
        if count == K:
            print(i)
            break