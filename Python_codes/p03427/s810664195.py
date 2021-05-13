N = int(input())

if N > 9:
    if (N%(int("1" + (len(str(N)) - 1)*"0"))) == int((len(str(N)) - 1) * "9"):
        tmp = list(str(N))
        tmp = [int(item) for item in tmp]
        print(sum(tmp))
    else:
        tmp = list(str(N - (N%(int("1" + (len(str(N)) - 1)*"0"))) - 1))
        tmp = [int(item) for item in tmp]
        print(sum(tmp))
else:
    print(N)


