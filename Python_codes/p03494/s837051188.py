N = int(input())
li = list(map(int,input().split()))
count = 0
while 1:
    if all([x%2==0 for x in li]):
        li = [int(x/2) for x in li]
        count+=1
    else:break
print(count)