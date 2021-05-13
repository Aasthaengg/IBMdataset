n, q = map(int, input().split())
s = input()

ml = [0 for i in range(n)]
for i in range(n-1):
    if s[i]+s[i+1] == 'AC':
        ml[i] = 1

def cumulative_sum(collection):
    result = [0]
    for item in collection:
        result.append(result[-1] + item)
    return result
csml = cumulative_sum(ml)

for i in range(q):
    l, r = map(int, input().split())
    print(csml[r-1] - csml[l-1] , flush=True)
