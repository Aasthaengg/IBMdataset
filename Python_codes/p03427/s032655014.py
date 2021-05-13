N = list(input())

nup = sorted(N)

if N[1:len(N)+1] == ["9"] * (len(N)-1):
    sum1 = 0
    for i in range(len(N)):
        sum1 += int(N[i])
    print(sum1)

else:
    print(9*(len(N)-1) + int(N[0])-1)
