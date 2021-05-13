x = int(input())
count = 1
for i in range(1,x+1):
    for n in range(2,10):
        if i**n <= x:count = max(i**n,count)
print(count)