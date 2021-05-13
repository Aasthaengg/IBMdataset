n,k=map(int, input().split()) 
a = range(1, n)
k = k - 1
print(len([a[i:i+k] for i in range(n-k)]))