S = input()
a = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

for i in S:
    if i in a:
        a.remove(i)
#print(a)
print(a[0] if len(a)!=0 else 'None')