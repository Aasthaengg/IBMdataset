s = list(input())
s.sort()
a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'r', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
for i in a:
    if i not in s:
        print(i)
        exit()
print('None')