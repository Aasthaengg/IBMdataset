S = input()

memo = []
memo.append(S[0])
p = 1

while p<len(S):
    if len(memo[-1])==2:
        memo.append(S[p])
        p += 1
    elif memo[-1]!=S[p]:
        memo.append(S[p])
        p += 1
    elif p+1==len(S):
        break
    else:
        memo.append(S[p:p+2])
        p += 2
print(len(memo))