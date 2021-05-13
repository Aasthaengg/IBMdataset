import collections
N = list(input())
cnt = 0
ans = []
for i in range(len(N)-1):
    if N[i] == N[i+1]:
        cnt += 1
    else:
        ans.append(cnt)
        cnt = 0
ans.append(cnt)
for i in ans:
    if i >= 2:
        print('Yes')
        exit()
print('No')  