from operator import itemgetter

def main():
    N,M = map(int, input().split())
    A = [[1,int(x)] for x in input().split()]
    for _ in range(M):
        b,c = map(int, input().split())
        A.append([b,c])
    A.sort(key=itemgetter(1))
    A.reverse()
    n=0
    s=0
    for a in A:
        n+=a[0]
        if n<=N:
            s+=a[1]*a[0]
        elif n>N:
            d=a[0]
            e=a[1]
            break
    s+=(N-n+d)*e
    print(s)
    
main()