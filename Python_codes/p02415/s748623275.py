letters=[str(x) for x in input().split(", ")]
list1=[]
for i in letters:
    list1.append(i.swapcase())
print(", ".join(list1))