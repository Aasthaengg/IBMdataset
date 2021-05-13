from collections import Counter
N,M = list(map(int,input().split()))

counter = Counter()
for i in range(M):
    counter.update(map(int,input().split()))

for count in counter.most_common():
    if count[1]%2 != 0:
        print("NO")
        break
else:
    print("YES")