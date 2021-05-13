n = int(input())

if n == 1:
    print('a')
    exit()

lst = ['a']
for i in range(n-1):
    new_lst = []
    for string in lst:
        num = ord(sorted(string)[-1])
        for j in range(ord('a'), num+2):
            new_lst.append(string+chr(j))
    lst = new_lst

for string in lst:
    print(string)