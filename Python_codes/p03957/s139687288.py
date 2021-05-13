s = input()
prev = -1
 
se = set()
for i in ['c','f']:
    for idx,j in enumerate(s):
        if j.lower() == i and idx > prev:
            se.add(j.lower())
            prev = idx
            break
            
print('Yes' if len(se) == 2 else 'No')