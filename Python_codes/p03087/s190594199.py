import copy

n, q = map(int, input().split())
s = input()

cnt = [0]
for i in range(n-1):
    if s[i] == 'A' and s[i+1] == 'C':
        cnt.append(cnt[-1] + 1)
    else:
        cnt.append(cnt[-1])

for i in range(q):
    l, r = map(int, input().split())
    print(cnt[r-1] - cnt[l-1])