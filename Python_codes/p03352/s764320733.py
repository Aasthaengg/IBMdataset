x = int(input())

li = [1]
for i in range(2,32):
    cnt = 2
    while i**cnt<=x:
        li += [i**cnt]
        cnt +=1

print(max(li))