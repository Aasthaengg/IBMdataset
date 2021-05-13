
n = int(input())

a = list()
a = input().split()

curr = 1
count = 0

for i in a:
    if int(i) == curr: 
        curr+=1
    elif int(i)!=curr:
        count+=1
if curr == 1:
    print("-1")
else:
    print(count)