n , d = map(int, input().split())
count = 0

for i in range(n):
    if n >= 2*d+1:
        count += 1
        n = n - (2*d+1)
#print(n)
if n != 0:
    count += 1
print(count)