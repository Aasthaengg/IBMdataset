#coding:UTF-8

def MP(n,a):
    minv=a[0]
    maxv=a[1]-a[0]
    for i in range(1,n):
        if maxv<a[i]-minv:
            maxv=a[i]-minv
        if minv>a[i]:
            minv=a[i]    
    print(maxv)
if __name__=="__main__":
    n=int(input())
    a=[]
    for i in range(n):
        a.append(int(input()))
    MP(n,a)