from collections import Counter

n = int(input())
v = list(map(int, input().split()))
odd = Counter(v[0::2])
even = Counter(v[1::2])
odd["$"] = 0
even["#"] = 0
ans = 0
if odd.most_common()[0][0] == even.most_common()[0][0]:
    if odd.most_common()[1][1] > even.most_common()[1][1]:
        ans = n - odd.most_common()[1][1] - even.most_common()[0][1]
    else:
        ans = n - odd.most_common()[0][1] - even.most_common()[1][1]
else:
    ans = n - odd.most_common()[0][1] - even.most_common()[0][1]
print(ans)