#coding:UTF-8
def Check(P,k,w):
    i=0
    for j in range(k):
        s=0
        while s+w[i]<=P:
            s+=w[i]
            i+=1
            if i==n:
                return n
    return i

def Allocation(n,k,w):
    left=0
    right=100000000000000
    while right-left > 1:
        mid=int((left+right)/2)
        v=Check(mid,k,w)
        if v>=n:
            right=mid
        else:
            left=mid
    print(right)
  
if __name__=="__main__":
    a=input()
    n=int(a.split(" ")[0])
    k=int(a.split(" ")[1])
    w=[]
    for i in range(n):
        w.append(int(input()))
    Allocation(n,k,w)