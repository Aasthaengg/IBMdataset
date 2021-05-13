a=input()
b=input()
c=input()

#l=a+b+c

#n=a[0]
#a=a.lstrip(n)
n='a'
while True: 
    if n=='a':
        if len(a)==0:
            print('A')
            exit()
            
        n=a[0]
        #a=a.lstrip(n)
        a=a[1:]
        
    elif n=='b':
        if len(b)==0:
            print('B')
            exit()
            
        n=b[0]
        #b=b.lstrip(n)
        b=b[1:]
        
    else:
        if len(c)==0:
            print('C')
            exit()
            
        n=c[0]
        #c=c.lstrip(n)
        c=c[1:]

