S = input()
for i in range(1, len(S)+1):
    tmp_S = S[:-i]
    if len(tmp_S) % 2 != 0:
        continue
    center = int(len(tmp_S) / 2)
    if tmp_S[:center] == tmp_S[center:]:
        print(len(tmp_S))
        break