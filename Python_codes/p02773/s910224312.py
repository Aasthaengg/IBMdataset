from collections import Counter

N = int(input())
S = [input() for i in range(N)]

C = Counter(S)

C = sorted(C.items(), key=lambda x:x[1], reverse=True)


cnt_max = C[0][1]
ans = []
for i in range(len(C)):
    if cnt_max > C[i][1]:
        break
    else:
        ans.append(C[i][0])

ans.sort()

for w in ans:
    print(w)