n=int(input())
lst=[2,1]
for i in range(86):
    lst.append(lst[i]+lst[i+1])
print(lst[n])