#100 C - /\/\/\/
import collections
n = int(input())
A = list(map(int,input().split()))

A1 = A[::2]
A2 = A[1::2]
cnt1 = collections.Counter(A1)
cnt2 = collections.Counter(A2)

items1 = list(cnt1.items())
items2 = list(cnt2.items())
items1 = sorted(items1,key = lambda x:x[1],reverse = True)
items2 = sorted(items2,key = lambda x:x[1],reverse = True)

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