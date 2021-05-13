S = list(map(int, input()))
K = int(input())
count = 0
for a in S:
    if a == 1:
        count += 1
        if count == K:
            print(1)
            exit()
    else:
        print(a)
        exit()
