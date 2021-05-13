#1st: Code Festival 2015 Qualifying B (0408)
if False:
    N,M=map(int,input().split())
    A=[int(i) for i in input().split()]
    B=[int(i) for i in input().split()]
    A.sort()
    B.sort()
    ans='YES'
    if N<M:
        ans='NO'
    else:
        while B:
            a=A.pop()
            b=B.pop()
            if b>a:
                ans='NO'
                break
    print(ans)

#2nd: CF2014QA-C
if False:
    A,B=map(int,input().split())
    def uruu(n):
        ret=0
        ret+=n//4
        ret-=n//100
        ret+=n//400
        return ret
    print(uruu(B)-uruu(A-1))

#3rd: Code Formula 2014 - C
if False:
    S=input()
    stack=list(S[::-1])
    # print(stack)
    user=[]
    s=stack.pop()
    while stack:
        # print(s)
        if s=="@":
            tmp=''
            x=stack.pop()
            while not(x in ('@',' ')):
                # print(x)
                tmp+=x
                if not stack:
                    break
                x=stack.pop()
            user.append(tmp)
            s=x
        else:
            s=stack.pop()
    user=list(set(user))
    user.sort()
    for u in user:
        if u:
            print(u)

#4th: Hitachi Programming Contest 2020 - A    
if False: 
    S=input()
    hi=['hi'*i for i in range(1,10)]
    print('Yes' if S in hi else 'No')

#5th: Keyence Programming Contest 2019 - C
if True:
    N=int(input())
    A=[int(i) for i in input().split()]
    B=[int(i) for i in input().split()]
    S=list(zip(A,B))
    if sum(A)<sum(B):
        print(-1)
    else:
        C=[]
        for s in S:
            a,b=s
            if a<b: C.append(s)
        CA=sum(C[i][0] for i in range(len(C)))
        CB=sum(C[i][1] for i in range(len(C)))
        S.sort(key=lambda x: x[0]-x[1])
        while CA<CB:
            c,d=S.pop()
            CA+=c
            CB+=d
            C.append((c,d))
        print(len(C))




