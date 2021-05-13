import itertools
import collections
N = int(input())
S = [input() for i in range(N)]
candi = []
for s in S:
    if s[0] == 'M' or s[0] == 'A' or s[0] == 'R' or s[0] == 'C' or s[0] == 'H':
        candi.append(s[0])
col_s = collections.Counter(candi)
combi_s = itertools.combinations(list(col_s),3)
counter = 0 
for i in combi_s:
    counter += col_s[i[0]]*col_s[i[1]]*col_s[i[2]]
print(counter)