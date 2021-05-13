n = int(input())
s = [tuple(map(int, input().split())) for _ in range(n)]
s = sorted(s, key=lambda x:x[1])

total = 0
for si in s:
    total += si[0]
    if total > si[1]:
        print('No')
        exit()
print('Yes')
