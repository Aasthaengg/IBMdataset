n = int(input())

lst = [2, 1]
for i in range(100):
    lst.append(lst[-1]+lst[-2])
print(lst[n])