import itertools
import copy
S = input()

ans = 0
for v in itertools.product([1,0], repeat=len(S)-1):
    S_copy = copy.deepcopy(S)
    idx = 0
    sum = 0
    for i in range(1,len(S)):
        if v[i-1] == 1:
            sum += int(S[idx:i])
            idx = i
    ans += int(S[idx:])
    ans += sum
print(ans)