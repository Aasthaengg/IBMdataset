n,k = [int(i) for i in input().split()]
an = input()
count = 1
n -= k
k -= 1
while(n > 0):
    n -= k
    count += 1
print(count)