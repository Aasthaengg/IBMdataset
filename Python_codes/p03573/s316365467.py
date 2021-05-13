list = list(map(int,input().split()))
list.sort()
if list.count(list[0])==1:
    print(list[0])
else:
    print(list[2])