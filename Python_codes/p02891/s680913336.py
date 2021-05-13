s = input()
k = int(input())
s = s + '0'

e = 1
l = []
for i in range(len(s)-1):
    if s[i]==s[i+1]:
        e+=1
    else:
        l.append(e)
        e=1

s = s[:-1]

if len(s)==1:
    print(k//2)    
else:
    if s[0]!=s[-1]:
        print(k*sum([i//2 for i in l]))
    else:
        if k==1:
            print(k*sum([i//2 for i in l]))
        else:
            if len(l)==1:
                print((k*l[0])//2)
            else:
                a = l.pop(0)
                b = l.pop(-1)
                l.append(a+b)
                print(k*sum([i//2 for i in l])-(a+b)//2+a//2+b//2)