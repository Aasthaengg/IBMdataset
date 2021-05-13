import re
s=input()
count=0
if re.search(r'a',s):
    count+=1
if re.search(r'b',s):
    count+=1
if re.search(r'c',s):
    count+=1
if count==3:
    print('Yes')
else:
    print('No')