#100 C - /\/\/\/ AC
import collections
n = int(input())
A = list(map(int,input().split()))

A1 = A[::2]
A2 = A[1::2]
cnt1 = collections.Counter(A1)
cnt2 = collections.Counter(A2)

items1 = list(cnt1.most_common())
items2 = list(cnt2.most_common())

if items1[0][0] != items2[0][0]:
    ans = (len(A1) - items1[0][1]) + (len(A2) - items2[0][1])
else:
    if len(items1) == len(items2) == 1:
        ans = min(len(A1),len(A2))

    else:
        ans1 = (len(A1) - items1[0][1]) + (len(A2) - items2[1][1])
        ans2 = (len(A1) - items1[1][1]) + (len(A2) - items2[0][1])
        ans = min(ans1,ans2)
print(ans)