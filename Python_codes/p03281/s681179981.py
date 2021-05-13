N = int(input())
count = 0
if N<105:
    print(0)
else:
    for i in range(105,N+1):
        yaku = 0
        if i%2 == 1:
            for j in range(1,i+1):
                if i%j == 0:
                    yaku += 1
            if yaku == 8:
                count += 1
    print(count)