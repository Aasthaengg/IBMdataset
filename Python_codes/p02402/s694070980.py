z = input()
r = input()
a = r.split(' ')    
list =[]
for i in a:
    list.append(int(i))
b = max(list)
c = min(list)
d = sum(list)
print('%s %s %s'%(c,b,d))