n = int(input())
k = len(str(n))
c = 0
for i in range(1,k):
    if i%2 == 1:
        c += 9*10**(i-1)
if k%2 == 1:
    c += n - 10**(k-1) + 1
print(c)