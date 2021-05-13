n = int(input())
ar = list(map(int,input().split(" ")))
count = 0
for i in range(0,n,2):
    if ar[i] % 2 == 1:
        count += 1
print(count)