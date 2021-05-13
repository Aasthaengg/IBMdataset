S = input()

ret = 9999999999
for i in range(len(S) - 2):
    target = int(S[i] + S[i+1] + S[i+2])
    diff = abs(target - 753)
    if diff < ret:
        ret = diff
print(ret)