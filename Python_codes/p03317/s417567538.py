n, k = list(map(int, input().split()))
a = list(map(int, input().split()))

i = a.index(1)

s = n

for j in range(i-k+1, i+k):
    if j < 0:
        continue
    elif j >= n:
        continue
    else:
        l = j
        u = (n-1-j)
        t = (l+k-2) // (k-1) + (u+k-2) // (k-1)
        #print(t)
        s = min(s, t)

print(s)