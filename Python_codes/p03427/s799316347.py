n = int(input())

lst = list(map(int,str(n)))
if len(lst) == 1:
    print(n)
elif set(lst[1:]) == {9}:
    print(lst[0] + 9*(len(lst)-1))
else:
    print((lst[0]-1) + 9*(len(lst)-1))