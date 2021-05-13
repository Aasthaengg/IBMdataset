n, m = map(int, input().split())
chk = [0]*(m+1)
for i in range(n):
    inp = list(map(int, input().split()))
    k = inp[0]
    for j in range(1,k+1):
        chk[inp[j]] += 1
print(chk.count(n))