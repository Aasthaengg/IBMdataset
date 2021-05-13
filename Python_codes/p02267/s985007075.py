#coding:UTF-8
def LS(n,S,q,T):
    count=0
    if n>q:
        for i in range(q):
            if T[i] in S:
                count+=1
    else:
        for i in range(n):
            if S[i] in T:
                count+=1
    print(count)
  
if __name__=="__main__":
    n=int(input())
    S=input().split(" ")
    q=int(input())
    T=input().split(" ")
    LS(n,S,q,T)