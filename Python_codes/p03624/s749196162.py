import collections
S=str(input())
cc=collections.Counter(S)
alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','m','o','p','q','r','s','t','u','v','w','x','y','z']

for i in range(26):
    if cc[alphabet[i]]==0:
        print(alphabet[i])
        exit()
    if i==25:
        print('None')
        exit()

