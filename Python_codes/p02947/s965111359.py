from collections import defaultdict
n = int(input())

def makeFreqTuple(s):
    freq = [0] * 26
    for c in s:
        freq[ord(c)-ord("a")] += 1
    return tuple(freq)

def C(n, k):
    numera = 1
    for i in range(n, n-k, -1):
        numera *= i
    denomi = 1
    for i in range(k, 1, -1):
        denomi *= i
    return numera // denomi

dic = defaultdict(int)
for i in range(n):
    s = input()
    t = makeFreqTuple(s)
    dic[t] += 1

ans = 0
for k, v in dic.items():
    ans += C(v, 2)
print (ans)