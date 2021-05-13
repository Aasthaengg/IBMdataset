import sys
li = list(input())
new_li = []
if len(li) == 1:
    print(1)
    sys.exit()
tmp = ''
for i,l in enumerate(li):
    if i == 0:
        new_li.append(li[0])
        continue
    if len(tmp)>0:
        new_li.append(tmp+l)
        tmp = ''
    elif new_li[-1] != l:
        new_li.append(l)
    else:
        tmp = l
print(len(new_li))