n = int(input())
hl = list(map(int,input().split()))

max_num = 0
for i in range(n):
    if hl[i] + 1 < max_num:
        print('No')
        exit()
    max_num = max(max_num, hl[i])
print('Yes')