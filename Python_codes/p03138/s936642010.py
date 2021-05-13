import sys
sys.setrecursionlimit(10**9)
INF=10**18
def input():
    return sys.stdin.readline().rstrip()

def main():
    N,K=map(int,input().split())
    A=list(map(int,input().split()))
    l=[0]*(len(str(bin(K)))-2)
    for a in A:
        for i in range(len(str(bin(a)))-2):
            if len(l)<=i:
                l.append(0)
            if (a >> i) & 0b1 == 1:
                l[i]+=1
    ans=0
    for j in reversed(range(max(len(l),len(str(bin(a)))-2))):
        if (K >> j) & 0b1 == 1:
            ans+=max(l[j],N-l[j])*(2**j)
        else:
            ans+=l[j]*(2**j)
    for i in range(len(bin(K))-3,0,-1):
        if (K >> i) & 0b1 == 1:
            tmp=0
            f=False
            for j in reversed(range(max(len(l),len(str(bin(a)))-2))):
                if j==i:
                    tmp+=l[j]*(2**j)
                    f=True
                else:
                    if f==True or (K >> j) & 0b1 == 1:
                        tmp+=max(l[j],N-l[j])*(2**j)
                    else:
                        tmp+=l[j]*(2**j)
            ans=max(ans,tmp)
    print(ans)
    
            

if __name__ == '__main__':
    main()
