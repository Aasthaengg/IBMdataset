n = int(input())
a = input().split()
b = [0] * n
for i in range(n):
    if i % 2 == 0:
        b[i//2] = a[n-1-i]
    else:
        b[n-(i+1)//2] = a[n-1-i]
print(' '.join(b))
