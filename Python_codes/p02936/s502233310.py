import sys
sys.setrecursionlimit(1000000)

def val_add(i,con,val):
    if con[i] :
        for j in con[i]:
            val[j]+=val[i]
            val_add(j,con,val)

def tree(i,con):
    if not con[i]: pass
    else :
        for j in con[i]:
            con[j].remove(i)
            tree(j,con)

def main():
    n,q=map(int,input().split())
    con=[[] for _ in range(n)]
    val=[0]*n
    for _ in range(n-1):
        a,b=map(int,input().split())
        con[a-1].append(b-1)
        con[b-1].append(a-1)

    tree(0,con)

    for _ in range(q):
        p,x=map(int,input().split())
        val[p-1]+=x

    val_add(0,con,val)


    print(" ".join(map(str,val)))

main()