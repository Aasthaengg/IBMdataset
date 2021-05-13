n, k = map(int, raw_input().split())
pb = n - (k + 1)
combi = 0
for b in range(k+1, n+1):
    combi += (n/b)*(b-k)
    if n % b >= k:
        combi += (n%b) - (k-1)
    if k == 0:
        combi -=1
print combi