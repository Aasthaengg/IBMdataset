n,d = map(int,input().split())
total = 2*d + 1
count = 1
while total < n:
    total += 2*d + 1
    count += 1
print(count)