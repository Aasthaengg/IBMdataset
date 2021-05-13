from collections import Counter

N, K = map(int, input().split())
a = list(map(int, input().split()))

sum = 0
c = Counter(a).most_common()
if K > len(c):
    print(0)
    exit()
for i in range(K):
    sum += c[i][1]
print(len(a) - sum)
