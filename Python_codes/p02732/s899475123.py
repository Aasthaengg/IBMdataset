from collections import Counter
n = int(input())
A = list(map(int, input().split()))
dict_A = Counter(A)
sum_comb = 0
for v in dict_A.values():
    sum_comb += int((v * (v - 1)) / 2)

for a in A:
    print(sum_comb - dict_A[a] + 1)