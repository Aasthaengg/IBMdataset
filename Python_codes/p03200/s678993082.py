S = list(input())
cnt = 0
ind = 0
for i,s in enumerate(S):
    if s == 'W':
        cnt += 1
        ind += i

last = sum(range(cnt))
print(ind-last)