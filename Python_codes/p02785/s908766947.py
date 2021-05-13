n,k = map(int,input().split())
if n < k: k = n
h = list(map(int,input().split()))
h = sorted(h,reverse = True)
for i in range(k):
    h[i] = 0
print(sum(h))