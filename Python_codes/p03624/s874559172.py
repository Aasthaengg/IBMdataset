S = list(input())
S.sort()
import bisect
a_uni = ord('a')

Search = S
for i in range(26):
    char = chr(a_uni+i)

    if Search and Search[0] == char:
        ind = bisect.bisect_right(S,char)
        Search = S[ind:]
        continue
    print(char)
    exit()
print('None')


