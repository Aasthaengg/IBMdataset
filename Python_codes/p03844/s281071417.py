a,b,c=[int(i)if i.isdigit() else i for i in input().split()]
print(a+c if b=="+" else a-c)