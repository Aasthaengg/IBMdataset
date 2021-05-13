N = int(input())
AA = [2,4,8,16,32,64]

if N >=64:
    print(64)

elif N in AA:
    print(N)

else:
    for i in range(6):
        num = AA[i]
        if num < N:
            pass

        elif num > N:
            print(round(num/2))
            break
