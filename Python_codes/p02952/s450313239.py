n = int(input())
count = 0

for i in range(1,n+1):
    lenth = len(str(i))
    if lenth % 2 == 1:
        count+= 1

print(count)