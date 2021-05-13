x = int(input())
num = list(map(int,input().split()))
min = num[0]
max = num[0]
for i in range(x):
    if num[i]<min:
        min=num[i]
    if max<num[i]:
        max=num[i]
print(min,max,sum(num),sep=" ")