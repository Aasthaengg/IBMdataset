# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_4_A
# Linear Search
# Result:
import sys


### main
ary_s_len = int(sys.stdin.readline().rstrip())
ary_s = [int(x) for x in sys.stdin.readline().rstrip().split(' ')]
ary_t_len = int(sys.stdin.readline().rstrip())
ary_t = [int(x) for x in sys.stdin.readline().rstrip().split(' ')]
assert len(ary_s) == ary_s_len
assert len(ary_t) == ary_t_len

count = 0
for e in ary_t:
    for se in ary_s:
        if e == se:
            count += 1
            break

print count