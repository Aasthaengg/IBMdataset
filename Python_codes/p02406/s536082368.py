n = int(input())
s = ''
for i in range(n):
    x = i+1
    if x%3==0:
        s += ' '+str(i+1)
        continue
    
    while x:
        if x%10==3:
            s += ' '+str(i+1)
            break
        x = x//10
print(s)

