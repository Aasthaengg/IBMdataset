import collections
N = int(input())
A =list(map(int,input().split()))
col_A = collections.Counter(A)
count = 0
for key,val in col_A.items():
    if key > val:
        count += val
    else:
        count += (val - key)
print(count)
