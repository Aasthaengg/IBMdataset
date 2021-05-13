def main():
    n = int(input())
    A = [[] for i in range(n)]
    ans = 0
    for i in range(n):
        a = int(input())
        tmp = {}
        for j in range(a):
            x,y = map(int,input().split())
            tmp[x-1] = y
        A[i] = tmp
    #print(A)
    for i in range(2**n):
        kouho = []
        for j in range(n):
            if  (i>>j)&1:
                kouho.append(j)
        honest = {}
        for j in range(n):
            if j in kouho:
                honest[j] = 1
            else:
                honest[j] = 0
        flag = True
        #print(kouho)
        for j in kouho:
            hatugen = A[j]
            for k in hatugen.keys():
                if honest[k]!=hatugen[k]:
                    flag = False
        if flag:
            ans = max(ans,len(kouho))
    print(ans)

main()