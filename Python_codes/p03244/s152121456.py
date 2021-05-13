def count(l):
    odd = {}
    even = {}
    for idx, d in enumerate(l):
        if idx%2 == 0:
            res = even
        else:
            res = odd
        if d in res:
            res[d] += 1
        else:
            res[d] = 1
    return odd, even
n = int(input())
data = list(map(int, input().split()))
odd, even = count(data)
odd = sorted(odd.items(), key=lambda x:-x[1])
even = sorted(even.items(), key=lambda x:-x[1])
if len(odd) == 1 and len(even) == 1:
    if odd[0][0] != even[0][0]:
        print(0)
    else:
        print(min(odd[0][1], even[0][1]))
else:
    size = n//2
    if odd[0][0] != even[0][0]:
        ans = 2*size - odd[0][1] - even[0][1]
        print(ans)
    else:
        ans1 = 2*size - odd[0][1] - even[1][1]
        ans2 = 2*size - odd[1][1] - even[0][1]
        print(min(ans1, ans2))