lis=[int(input())]
for i in range(1000):
    if lis[i]%2==0:
        a=lis[i]//2
        lis.append(a)
        def has_duplicates(x):
            return len(x) != len(set(x))
        if has_duplicates(lis)==True:
            break
    else:
        a=lis[i]*3+1
        lis.append(a)
        def has_duplicates(x):
            return len(x) != len(set(x))
        if has_duplicates(lis)==True:
            break
print(len(lis))