from collections import Counter

N = int(input())

A = list(map(int, input().split()))

dic = Counter(A)

res = 0
for i, cnt in dic.items():
    res += cnt*(cnt-1)//2


for i in A:
    temp = dic[i]-1
    print(res-temp)