a,b,k =  input().split()
a = int(a)
b = int(b)
k = int(k)

if a + b < k:
    i = 0
    m = 0
elif a <= k:
    i = 0
    m = b - (k-a)
else:
    i = a-k
    m=b
print(i,m)