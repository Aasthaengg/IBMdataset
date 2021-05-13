from collections import Counter

n = int(input())
a = list(map(int,input().split()))
q = int(input())
freq = Counter(a)
sm = sum(a)
for i in range(q):
    b,c = map(int,input().split())
    bn = freq[b]
    freq[b] = 0
    if c in freq:
        freq[c] += bn
    else:
        freq[c] = bn
    sm = sm + (c-b)*bn
    print(sm)