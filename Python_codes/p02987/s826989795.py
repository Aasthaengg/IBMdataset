import collections
dict_values = []


S = input()

c = collections.Counter(S)

d = len(c)


f = list(c.values())



if (d==2) and f[0]==f[1]:
    print("Yes")
    
else:
    print("No")