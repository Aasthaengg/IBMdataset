N =int(input())
if N<=2:
    print(0)
    exit()

count = 0
while N >=6:
    N-=3
    count+=1
count+=1
print(count)
