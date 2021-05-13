s = input()
l1 = ['D','R','U']
l2 = ["D",'L','U']
count = 0

for i in s[::2]:
    if i in l1 :
        count += 1
for i in s[1::2]:
    if i in l2:
        count += 1
    
if count == len(s):
    print('Yes')
else:
    print('No')