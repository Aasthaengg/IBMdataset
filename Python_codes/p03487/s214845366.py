import collections

n = int(input())
A = list(map(int,input().split()))

cnt = collections.Counter(A)

ans = 0
for key, value in cnt.items():
    if value < key:
        ans += value
    elif key < value:
        ans += value-key
        
print(ans)