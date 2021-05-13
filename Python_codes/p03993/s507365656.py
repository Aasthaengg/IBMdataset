n = int(input()) #兎の数
a = list(map(int,(input().split())))
a = {i+1: v for i, v in enumerate(a)}
#print(a)
#print(a[1])

counter = 0

for i,j in a.items():
    if i == a[j]:
        #print(i,j)
        counter += 1

print(counter//2)