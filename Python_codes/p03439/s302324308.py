N = int(input())

def f():
    lb = 0
    ub = N - 1
    
    print(lb, flush=True)
    lba = input()
    if lba == 'Vacant': return
    
    print(ub, flush=True)
    uba = input()
    if uba == 'Vacant': return
    
    while lb < ub:
        qry = (lb + ub) // 2
        print(qry, flush=True)
        qa = input()
        if qa == 'Vacant': return
        if (not ((lb ^ qry) & 1) and lba == qa) or (((lb ^ qry) & 1) and lba != qa):
            lb = qry
            lba = qa
        else:
            ub = qry

f()