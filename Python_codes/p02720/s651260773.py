K = int(input())
ans_list = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
nex = ans_list.copy()


def resp(n):
    if n == "0":
        return ["0", "1"]
    elif n == "9":
        return ["8", "9"]
    else:
        n_tmp = int(n)
        return [n, str(n_tmp + 1), str(n_tmp - 1)]


for j in range(1000):
    tmp = nex.copy()
    nex = []
    for i in tmp:
        nex += [i + x for x in resp(i[-1])]
    ans_list += nex
    if len(ans_list) > 10 ** 5:
        break

ans_list = list(map(int, ans_list))
ans_list.sort()
print(ans_list[K - 1])
