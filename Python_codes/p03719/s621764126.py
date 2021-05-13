A,B,C=map(int,input().split())

def J(A,B,C):
    if C>=A and C<=B:
        return 'Yes'
    else:
        return 'No'
    
print(J(A,B,C))