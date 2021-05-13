n = int(input())
a = list(map(int, input().split()))

def test(total, res):
    for i in a[1:]:
        hugou = total > 0
        total += i
        if hugou:
            if total>=0:
                res += abs(total)+1
                total = -1
        else:
            if total<=0:
                res += abs(total)+1
                total = 1
    return res

    
res = 0
total = a[0]
if a[0]<=0:
    total = 1
    res += abs(a[0])+1
res1 = test(total, res)

res = 0
total = a[0]
if a[0]>=0:
    total = -1
    res += abs(a[0])+1
res2 = test(total, res)

print(min(res1, res2))