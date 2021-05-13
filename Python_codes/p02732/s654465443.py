from collections import Counter
N = int(input())
A = list(map(int, input().split()))
total = 0

cnt = Counter(A)
for i in cnt:
    total+=int(((cnt[i])*(cnt[i]-1))/2)

for i in range(N):
    t = cnt[A[i]]
    print(int(total - (t*(t-1)/2) + ((t-1)*(t-2)/2)))