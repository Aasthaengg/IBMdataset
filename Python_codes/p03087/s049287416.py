n, q = map(int, input().split())
s = input()
ls = [0] * n
cnt = 0
for i in range(1, n):
    if s[i] == 'C' and s[i-1] == 'A':
        cnt += 1
    ls[i] += cnt
for j in range(q):
    l, r = map(int, input().split())
    print(ls[r-1]-ls[l-1])
