a=[int(i)for i in input().split()]
b=a.pop(a.index(max(a)))
if sum(a)==b:
    print("Yes")
else:
    print("No")