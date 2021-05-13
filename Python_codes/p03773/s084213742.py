a,b=map(int,input().split())

if b+a>23:
    s=b-(24-a)
else:
    s=a+b
    
print(s)