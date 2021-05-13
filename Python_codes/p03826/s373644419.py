
lst = list(map(int,input().split()))
if lst[0]*lst[1] >= lst[2]*lst[3]:
    print(lst[0]*lst[1])
else:
    print(lst[2]*lst[3])