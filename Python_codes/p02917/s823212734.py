# input
n = int(input())
a = [0 for i in range(n)]
b = [int(i) for i in input().split()]

# main
a[0] = b[0]
for i in range(1, n-1):
  a[i] = min(b[i-1], b[i])
a[n-1] = b[n-2]

# output
print(sum(a))
