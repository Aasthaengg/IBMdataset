x = int(input())
c = 0
n = x
while(True):
    if n%360 == 0:
        c+=1
        break
    c+=1
    n+=x
print(c)