k = int(input())
odd = 1; even = 1
if k % 2 == 0:
    odd = k // 2; even = k // 2
else:
    odd = (k+1) // 2; even = (k-1) // 2
print(odd * even)