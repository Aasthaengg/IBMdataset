A,B,C=map(int,input().split())
kot=0
"""while C!=0:

    if B+A==0:
        kot+=1
        break
    else:
        C-=1
        kot+=1
        if B>0:
            B-=1
            kot+=1
        elif A>0:
            A-=1
if B>0:
    kot+=B

print(kot)"""
if C>=B:
    kot+=B*2
    C-=B
else:
    kot+=B+C
    print(kot)
    exit()
if C-1>A:
    kot+=A+1
else:
    kot+=C
print(kot)