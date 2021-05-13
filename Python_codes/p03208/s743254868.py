n,k=map(int,input().split())
h=[int(input()) for _ in range(n)]
h.sort()
diff=[0]*(n-k+1)
for m in range(n-k+1):
  diff[m] = h[m+k-1]-h[m]
print(min(diff))