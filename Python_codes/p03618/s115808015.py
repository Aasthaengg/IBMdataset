from sys import stdin 
a = stdin.readline().rstrip()
n = len(a)
k = [0]*26
a = sorted(a)
t = "a"
tmp = 0
for i in range(n):
    if t == a[i]:
        k[tmp] += 1
    else:
        t = a[i]
        tmp += 1
        k[tmp] += 1
answer = (n*(n-1)) // 2
for i in range(26):
    if k[i] > 1:
        answer -= (k[i]*(k[i]-1)) // 2
print(answer + 1)