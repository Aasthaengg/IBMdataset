sel='E'
#A
if sel=='A':
    N,M=map(int,input().split())
    ans=0
    ans+=M*(M-1)//2
    ans+=N*(N-1)//2
    print(ans)

#B
if sel=='B':
    def ispal(s):
        for i in range(len(s)//2+1):
            if s[i]!=s[-(i+1)]:
                return False
        return True

    S=input()
    N=len(S)
    if ispal(S) and ispal(S[:(N-1)//2]) and ispal(S[(N+3)//2-1:]):
        print('Yes')
    else:
        print('No')

#C
if sel=='C':
    L=int(input())
    print((L**3)/27)

#D
if sel=='D':    
    N=int(input())
    A=[int(i) for i in input().split()]
    kin=list(set(A))
    cnt={}
    for k in kin:
        cnt[k]=0
    for a in A:
        cnt[a]+=1
    SUM=0
    for k in kin:
        SUM+=cnt[k]*(cnt[k]-1)//2
    for a in A:
        if cnt[a]>=2:
            print(SUM-cnt[a]+1)
        else:
            print(SUM)
        
#E
if sel=='E':
    def add(in1, in2):
        return [a + b for a, b in zip(in1, in2)]

    def split(ar, k, w):
        a = 0
        if max(max(ar)) > k:
            return -1
        tm = ar[0]
        for i in range(1, w):
            tm = add(tm, ar[i])
            if max(tm) > k:
                a += 1
                tm = ar[i]
        return a        

    h, w, k = map(int, input().split())
    s = [[int(i) for i in input()] for j in range(h)]
    ans = h*w

    for i in range(2**(h-1)):
        data = []
        temp = s[0]
        sp = bin(i+2**h)[4:]
        for j in range(1, h):
            if sp[j-1] == "0":
                temp = add(temp, s[j])
            else:
                data.append(temp)
                temp = s[j]
        data.append(temp)
        ans_ = split([list(x) for x in zip(*data)], k, w)
        if ans_ == -1:
            continue
        ans_ += sp.count("1")
        if ans > ans_:
            ans = ans_
    print(ans)



# #F
# if sel=='F':
#     N,S=map(int,input().split())
#     A=[int(i) for i in input().split()]
    

