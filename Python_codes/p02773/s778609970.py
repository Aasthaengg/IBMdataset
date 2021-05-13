import collections
import itertools
N = int(input())
P = [input() for i in range(N)]
ans =[]

counter = collections.Counter(P)
mode_v = counter.most_common()[0][-1]
it = list(itertools.takewhile(lambda kv: kv[-1] == mode_v, counter.most_common()))
for i in range(len(it)):
    ans.append(it[i][0])
s_ans = sorted(ans)
for i in range(len(s_ans)):
    print(s_ans[i])