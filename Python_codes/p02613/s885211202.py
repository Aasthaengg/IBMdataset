from collections import Counter
from typing import List

n = int(input())
s = [input() for _ in range(n)]
# print(s)
count = Counter(s)
'''
c0 = count['AC']
c1 = count['WA']
c2 = count['TLE']
c3 = count['RE']
'''


def ans(result: str):
    num = count[result]
    print(result, ' x ', str(int(num)))


ans('AC')
ans('WA')
ans('TLE')
ans('RE')
