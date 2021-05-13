from collections import Counter

N = int(input())
S = [input() for i in range(N)]

SC = Counter(S)
maxval = max(SC.values())
listmaxval = [key for key in SC if SC[key] == maxval]
listmaxval.sort()
ans = "\r\n".join(listmaxval)
print(ans)