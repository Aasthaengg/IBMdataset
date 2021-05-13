import collections

def answer(ds, ts):
    dsDic = collections.Counter(ds)
    tsDic = collections.Counter(ts)
    for k, v in tsDic.items():
        if dsDic.get(k) is None: return 'NO'
        if tsDic[k] > dsDic[k]:
            return 'NO'
    return 'YES'

n = int(input())
ds = list(map(int, input().split()))
m = int(input())
ts = list(map(int, input().split()))
print(answer(ds, ts))