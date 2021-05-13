import sys
import collections

N = int(input())
Ans = 111

while True:
    if len(collections.Counter(list(str(Ans)))) == 1 and Ans >=  N:
        print(Ans)
        sys.exit()
    else:
        Ans += 1