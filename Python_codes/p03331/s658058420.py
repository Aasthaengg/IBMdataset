n = int(input())
sum = float('inf')
 
for i in range(1, n):
    k = 0
    for j in range(len(str(i))):
        k += float(str(i)[j])
    for l in range(len(str(n-i))):
        k += float(str(n-i)[l])
    sum = min(sum, k)
 
print(int(sum))