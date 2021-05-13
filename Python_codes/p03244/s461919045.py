from collections import Counter

n = int(input())
v = [int(x) for x in input().split()]

odd = sorted(Counter(v[0:n:2]).items(), reverse=True, key=lambda x: x[1])
even = sorted(Counter(v[1:n+1:2]).items(), reverse=True, key=lambda x: x[1])

if odd[0][0] != even[0][0]:
    res = n - odd[0][1] - even[0][1]
elif len(odd) == 1:
    res = odd[0][1]
else:
    if odd[0][1] == even[0][1]:
        if odd[1][1] >= even[1][1]:
            res = n - odd[1][1] - even[0][1]
        else:
            res = n - odd[0][1] - even[1][1]
    elif odd[0][1] > even[0][1]:
        res = n - odd[0][1] - even[1][1]
    else:
        res = n - odd[1][1] - even[0][1]

print(res)
