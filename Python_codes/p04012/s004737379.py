import sys
w=input()
count={}
for i in w:
    count.setdefault(i,0)
    count[i]+=1
for j in count.values():
    if j%2!=0:
        print('No')
        sys.exit()
print('Yes')
