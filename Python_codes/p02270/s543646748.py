n, k  = map(int, input().split())
w = []
def check(ptest):
    tk=1
    p=0
    global k
    global w
    global n
    i=0
    
    while i<n:
        p+=w[i]
        if p<=ptest:
            i+=1
        else:
            tk+=1
            p=0
            
        if tk>k:
            return 0
            #break   
    
    return 1
for i in range(n):
    w.append(int(input()))
pmax = sum(w)
pmin = pmax//k - 1


while (pmax - pmin) > 1:
    pmid = (pmax + pmin)//2
    if check(pmid) == 1:
        pmax = pmid
    else:
        pmin = pmid
print(pmax)
