n, k = input().split()
n = int(n)
k = int(k)
a = [int(s) for s in input().split()]
sums = []
K = k - 1
for i in range(K,n - 1):
    if(a[i - K] < a[i + 1]):
        print("Yes")
    else:
        print("No")