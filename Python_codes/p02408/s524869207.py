from collections import defaultdict

trump = {
    'S': set(range(1, 14)),
    'H': set(range(1, 14)),
    'C': set(range(1, 14)),
    'D': set(range(1, 14)),
}
taro_trump = defaultdict(set)

n = int(input())
for i in range(n):
    (mark, num) = tuple(input().split(' '))
    num = int(num)
    taro_trump[mark].add(num)

no_taro_trump = defaultdict(set)
no_taro_trump['S'] = trump['S']
no_taro_trump['H'] = trump['H']
no_taro_trump['C'] = trump['C']
no_taro_trump['D'] = trump['D']

if 'S' in taro_trump:
    no_taro_trump['S'] = trump['S'] - taro_trump['S']
if 'H' in taro_trump:
    no_taro_trump['H'] = trump['H'] - taro_trump['H']
if 'C' in taro_trump:
    no_taro_trump['C'] = trump['C'] - taro_trump['C']
if 'D' in taro_trump:
    no_taro_trump['D'] = trump['D'] - taro_trump['D']

for mark in ['S', 'H', 'C', 'D']:
    for num in list(no_taro_trump[mark]):
        print(mark, num)