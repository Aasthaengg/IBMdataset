a, b, k = [int(w) for w in input().split()]
 
ak = a + k
bk = b - k + 1
 
for i in range(a, min(ak, b+1)):
    print(i)
for i in range(max(ak, bk), b + 1):
    print(i)