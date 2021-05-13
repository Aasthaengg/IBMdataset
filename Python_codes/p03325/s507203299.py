n = int(input())
a = list(map(int,input().split()))

count = 0
for i in range(len(a)):
    aa = a[i]
    while True:
        b,c = divmod(aa,2)
        if c != 0:break
        count += 1
        aa = b
print(count)