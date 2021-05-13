s = input()
r = 0
l = list(s)
for i in range(1 << len(s)-1):
    li = []
    for j in range(len(s)):
#         print(i,j)
        li += l[j]
        if j != len(s)-1:
            if i & 1 <<j:
                li += ['+']
#     print(li)
        
    r += eval(''.join(li))
print(r)