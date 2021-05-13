S = list(input())

SS = [0] * 26

lis = [chr(i) for i in range(97, 97 + 26)]

for S in S:
    ind = lis.index(S)
    if SS[ind] == 0:
        SS[ind] = 1
    else:
        print("no")
        break
else:
    print("yes")