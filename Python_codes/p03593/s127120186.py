import sys
def main():
    H,W,*B=sys.stdin.read().split()
    H,W=int(H),int(W)
    A=[]
    for b in B: A+=list(b)
    from collections import Counter
    C=Counter(A)
    a4,a2,a1=0,0,0
    for v in C.values():
        d,m=divmod(v,4)
        a4+=d
        d,m=divmod(v,2)
        a2+=d
        a1+=m
    if a4 * 4 >= (H-(H&1))*(W-(W&1)) and a1 <= H&W&1:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()

