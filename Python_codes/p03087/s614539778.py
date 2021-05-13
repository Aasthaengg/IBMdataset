n, q = map(int, input().split())
s = input()
cnt = 0
cumsum = [0,0]
for i in range(n-1):
    if s[i] == 'A' and s[i+1] == 'C':
        cnt += 1
    cumsum.append(cnt)
for _ in range(q):
    l, r = map(int, input().split())
    print(cumsum[r] - cumsum[l])