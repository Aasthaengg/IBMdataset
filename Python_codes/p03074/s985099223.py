from sys import stdin
def main():
    #入力
    readline=stdin.readline
    N,K=map(int,readline().split())
    S=readline().strip()

    li=[]
    i=0
    now=0
    if S[0]=="0":
        li.append(0)
    while i<len(S):
        if S[i]=="1":
            while True:
                if S[i]=="1":
                    now+=1
                    i+=1
                    if i==len(S):
                        break
                else:
                    break
        elif S[i]=="0":
            while True:
                if S[i]=="0":
                    now+=1
                    i+=1
                    if i==len(S):
                        break
                else:
                    break
        li.append(now)
        now=0
                
    #累積和
    for i in range(len(li)):
        if i==0:
            continue
        else:
            li[i]+=li[i-1]

    res=0
    if len(li)>=2*K+1:
        for left in range(0,len(li),2):
            if left==0:
                res=li[2*K]
            else:
                res=max(res,li[min(2*K+left,len(li)-1)]-li[left-1])
    else:
        res=li[-1]
    print(res)
    
if __name__=="__main__":
    main()