n = input()
f = 0

for i in range(len(n)):
    if n[i] in '9':
        f = 1
    
if f == 1:
    print('Yes')
else:
    print('No')