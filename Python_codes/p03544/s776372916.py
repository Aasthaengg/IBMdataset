l=[2,1]
for _ in range(85): l+=[l[-2]+l[-1]]
print(l[int(input())])