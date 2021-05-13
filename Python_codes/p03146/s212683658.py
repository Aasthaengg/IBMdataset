S = int(input())
S_lst = [S]

for i in range(10**5):
    if S_lst[i] % 2 == 0:
        S_lst.append(S_lst[i] / 2)
    else:
        S_lst.append(3 * S_lst[i] + 1)
    if S_lst[i+1] in S_lst[:-1]:
        print(i+2)
        break