from collections import Counter
n,m = map(int, input().split())
ka = []
for i in range(n):
    ka1 = list(map(int, input().split()))
    ka += ka1[1:]
ka = Counter(ka).most_common()
num = 0
for h in range(len(ka)):
    if ka[h][1] == n:
        num += 1
    else:
        break
print(num)