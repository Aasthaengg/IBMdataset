N = int(input())

n = int(N/1.08)
while int(n*1.08) <= N:
    if int(n*1.08) == N:
        print(n)
        break
    else:
        n += 1
else:
    print(":(")