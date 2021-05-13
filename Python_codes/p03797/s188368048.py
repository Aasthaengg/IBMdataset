S,C=map(int,input().split())
count=0
if C>=2*S:
    C-=S*2
    count+=S
    
    count+=C//4
    
else:
    count+=C//2
    
print(count)
