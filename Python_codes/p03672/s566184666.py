S = list(input())
for i in range(len(S)//2):
    flag =0
    _ = S.pop(-1)
    _ = S.pop(-1)
    bf = S[:len(S)//2]
    af = S[len(S)//2:]
    for i in range(len(bf)):
        if bf[i] != af[i]:
            flag = 1
            break
    if flag ==0:
        break
print(len(S))
