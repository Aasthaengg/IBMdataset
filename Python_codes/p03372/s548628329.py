from itertools import accumulate
import sys
input = sys.stdin.readline

def main():
    n,c = map(int,input().split())
    x1,v1 = [0],[0]
    for _ in range(n):
        a,b = map(int, input().split())
        x1.append(a)
        v1.append(b)
    x2 = [0]
    v2 = [0]
    for i in range(n,0,-1):
        x2.append(c-x1[i])
        v2.append(v1[i])

    v1, v2 = list(accumulate(v1)), list(accumulate(v2))
    g1,g2 = [v2[0]-x2[0]],[v2[0]-2*x2[0]]
    for i in range(1,n+1):
        f = v2[i] - x2[i]
        f2 = v2[i] - 2*x2[i]
        g1.append(max(g1[i-1],f))
        g2.append(max(g2[i-1],f2))
    val = max(v1[n]-x1[n] + g2[0], v1[n]-2*x1[n] + g1[0])
    for i in range(1,n+1):
        val = max(val, v1[n-i]-x1[n-i] + g2[i], v1[n-i]-2*x1[n-i] + g1[i])

    print(val)

if __name__=='__main__': main()