S = input()
res = 0
w_ind = 0
for i, s in enumerate(S):
    if s == "B":
        pass
    elif s == "W":
        res += i - w_ind
        w_ind += 1
print(res)
