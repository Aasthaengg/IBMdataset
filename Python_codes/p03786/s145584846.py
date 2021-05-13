sel=4
#ICC-D3-J
if sel==1: print('Judgement')

#ARC030-A
if sel==2:
    N=int(input())
    K=int(input())
    if 2*K-1<N:
        print('YES')
    else:
        print('NO')

#AGC004-A
if sel==3:
    A,B,C=map(int,input().split())
    ans=10**19
    whole=A*B*C
    for a in range(A//2,A//2+2):
        ans=min(ans,abs(whole-a*B*C*2))
    for b in range(B//2,B//2+2):
        ans=min(ans,abs(whole-A*b*C*2))
    for c in range(C//2,C//2+2):
        ans=min(ans,abs(whole-A*B*c*2))
    print(ans)

#AGC011-B
if sel==4:
    import bisect

    #O(N): 長さNの配列に対する累積和(+演算)
    def CS1D(lis): #listを渡す
        ret=[lis[0]]
        for i in range(1,len(lis)):
            ret.append(ret[i-1]+lis[i])
        return ret

    N=int(input())
    A=[int(i) for i in input().split()]
    A.sort()
    CS=CS1D(A)
    ans=0
    # print(A)
    # print(CS)
    # 各Aiに対して、x<=2*Aiを満たすAの最大の元Ajをとって,Ajについても同様にする。
    # こうして、変らなくなるか最後まで行ったら終わり。
    for i in range(N):
        # print('!',i)
        prev=-1
        size=CS[i]
        k=i
        while prev!=k:
            prev=k
            # print(size)
            k=bisect.bisect(A,2*size)-1 #ここまで食べれる
            # print(bisect.bisect(A,2*size))
            size=CS[k]
            if k==N-1:
                ans+=1
                break
    print(ans)
