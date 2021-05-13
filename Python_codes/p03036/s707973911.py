r,d,x = map(int, input().split())
mylist = [0] * 11
mylist[0] = x
for i in range(1,11):
    mylist[i] = r * mylist[i-1] - d
    print(mylist[i])