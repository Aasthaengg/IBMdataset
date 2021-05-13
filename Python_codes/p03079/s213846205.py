ABC = input().split()
list_ABC= list(ABC)

if list_ABC[0] == list_ABC[1] and list_ABC[0] == list_ABC[2]:
    print('Yes')
else:
    print('No')