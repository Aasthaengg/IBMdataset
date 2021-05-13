s = input()
alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
l = []
for i in alpha:
    if i not in s:
        l.append(i)

if len(l) == 0:
    print('None')
else:
    print(l[0])