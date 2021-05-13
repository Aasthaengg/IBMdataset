a = input().strip().split(" ")
lst = []
for i in range(len(a)):
    lst.append(int(a[i]))
b = set(lst)
print(len(b))