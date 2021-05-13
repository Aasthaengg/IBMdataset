lists=input().split()
lists.sort()
for list in lists:
    if list==lists[-1]:
        print(list)
    else:
        print(list,end=" ")