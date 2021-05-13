from collections import Counter
N, K = map(int, input().split())
A = Counter(list(map(int,input().split()))).most_common()
repeat = len(set(A))-K
ans = 0
num = 0

while num < repeat:
    ans += A.pop(-1)[1]
    num += 1

print(ans)