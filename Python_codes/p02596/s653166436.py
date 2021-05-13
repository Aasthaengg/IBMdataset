k = int(input())
sevens = 7 % k

if k % 2 ==0:
    print(-1)
else:
    for i in range(k):
        if sevens % k ==0:
            print(i+1)
            break
        else:
            sevens = (sevens*10 + 7) % k
    else:
        print(-1)