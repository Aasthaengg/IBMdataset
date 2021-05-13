def main():
    N,K=map(int,input().split())
    p=list(map(int,input().split()))

    E=[]

    for i in p:
        E.append((1+i)/2)

    S=[0]

    s=0
    for i in E:
        s+=i
        S.append(s)

    max=0
    right=0
    left=right+K

    while left<len(S):
        res=S[left]-S[right]
        if res>=max:
            max=res
        right+=1
        left=right+K

    print(max)

if __name__=="__main__":
    main()
