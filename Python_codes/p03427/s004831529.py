N = input()
Dig = len(N)
num = None
if Dig == 1:
    print(N)
else:
    for i in range(Dig-1):
        if N[i+1] != str(9):
            num = i
            break
        else:
            continue
    list_num = list(N)
    if not num == None:
        target = int(list_num[num]) -1
        array = list(map(int,N))
        ans = sum(array[:num]) + target + 9*(Dig-num-1)
        print(ans)
    else:
        array = list(map(int,N))
        print(sum(array))