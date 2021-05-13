from sys import stdin
n = int(stdin.readline().rstrip())
a = list(map(int,stdin.readline().rstrip().split()))
b = list(map(int,stdin.readline().rstrip().split()))
A = sum(a);B = sum(b)
count_1 = 0
count_2 = 0
total = B-A
for i,j in zip(a,b):
    if i < j:
        count_1 += (j-i+1)//2
    else:
        count_2 += i-j
count = max(count_1,count_2)
if count <= total:
    print("Yes")
else:
    print("No")