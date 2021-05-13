MM = input().split()
a = int(MM[0])
b = int(MM[1])
list1 = [str(a)*b,str(b)*a]
list1.sort()
print(list1[0])