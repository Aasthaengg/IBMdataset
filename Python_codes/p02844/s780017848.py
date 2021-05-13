N = int(input())
S = [str(i) for i in input()]

search = [("00"+str(s))[-3:] for s in range(0,1000)]
ans = []
for num in search:
    tmp_S = S
    if num[0] in tmp_S:
        tmp_S = tmp_S[tmp_S.index(num[0])+1:] 
    else:
        continue
    if num[1] in tmp_S:
        tmp_S = tmp_S[tmp_S.index(num[1])+1:] 
    else:
        continue
    if num[2] in tmp_S:
        ans.append(num)

print(len(ans))