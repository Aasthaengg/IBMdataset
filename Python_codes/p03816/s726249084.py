import itertools
N = int(input())
A = [int(x) for x in input().split()]
A.sort()
B = itertools.groupby(A)
cnt1 = 0
cnt2 = 0
for key, group in B:
    if len(list(group))%2==1:
      cnt1+=1
    else:
      cnt2+=1
print(cnt1+cnt2//2*2)