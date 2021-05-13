S = input()
K = int(input())

tmp = 1
tmp_idx = -1
for i in range(len(S)):
    if S[i] != "1":
        tmp = S[i]
        tmp_idx = i
        break
if tmp_idx == -1:
    print(1)
else:
    if K > tmp_idx:
        print(tmp)
    else:
        print(1)
