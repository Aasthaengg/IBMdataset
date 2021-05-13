box = []
elem = input().split()
for i in elem:
    if i == '+' or i == '-' or i =='*':
        v = '{0} {1} {2}'.format(box[-2],i,box[-1])
        box.pop()
        box.pop()
        box.append(eval(v))
    else:
        box.append(i)
print (box[0])