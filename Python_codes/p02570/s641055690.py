d, t, s = input().split() 

d=int(d)
t=int(t)
s=int(s)

if d == 0:
    print ('error')
    
elif t == 0:
    print ('error')
        
elif s == 0:
    print ('error')

else:
    
    if (s*t) >= d :
        print ('Yes')
    
    else:
        print ('No')
