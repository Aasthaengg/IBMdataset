mylist = list(map(int,input().split()))
mylist = list(dict.fromkeys(mylist))
print(len(mylist))