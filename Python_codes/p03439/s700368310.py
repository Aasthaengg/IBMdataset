N = int(input())

def q(n):
    print(n, flush=True)
    ans = input()
    if ans == 'Vacant': quit()
    return ans

def f():
    lb = 0
    ub = N
    lba = q(lb)
    while ub - lb > 1:
        qry = (lb + ub) // 2
        qa = q(qry)
        if (not ((lb ^ qry) & 1) and lba == qa) or (((lb ^ qry) & 1) and lba != qa):
            lb = qry
            lba = qa
        else:
            ub = qry
f()