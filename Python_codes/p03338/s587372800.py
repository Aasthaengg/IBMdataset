#7 B - Cut and Count
N = int(input())
S = list(input())

mcnt = 0
for i in range(N-1):
    count = 0
    l = S[:i]
    r = S[i:]
    l = set(l)
    r = set(r)
    for j in l:
        if j in r:
            count += 1
    mcnt = max(mcnt,count)
print(mcnt)