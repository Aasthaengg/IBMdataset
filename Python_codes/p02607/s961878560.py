kosuu = input()
lis = [int(i) for i in input().split()]
count=0

for i in range(1,len(lis)+1):
    if i%2 ==1:
        if lis[i-1] %2 ==1:
            count +=1
print(count)