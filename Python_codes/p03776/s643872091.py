def comb(n,m):
    ans = 1
    if n==0 or m == 0:
        return 0
    else:
        for i in range(m):
            j = n-i
            ans *= j
        for i in range(1,m+1):
            ans //= i
        return ans
    
def main():
    import sys
    input = sys.stdin.readline
    N,A,B = map(int,input().split())
    V = list(map(int,input().split()))
    #N,A,B = 50,1,50
    #V = [1]*50
    V = sorted(V)[::-1]
    maxAv = sum(V[:A])/A
    maxB = A
    for i in range(A+1,B+1):
        tmp = sum(V[:i])/i
        if maxAv == tmp:
            maxB = i
    count = 0
    
    C = []
    now = V[0]
    c = 0
    for i in V:
        if now == i:
            c += 1
        else:
            C.append([now,c])
            now = i
            c = 1
    if c != 0:
      C.append([now,c])
    C = sorted(C,key=lambda a: a[0])[::-1]
    for i in range(A,maxB+1):
        pretmp = 0
        tmp = 0
        now = 0
        for j in C:
            if tmp >= i:
                break
            now = j[1]
            pretmp = tmp
            tmp += now
        count += comb(now, i-pretmp)
    #print(C)
    print(maxAv)    
    print(count)
            
    
main()