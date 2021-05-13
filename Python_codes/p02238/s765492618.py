#coding:utf-8
        
def DFS(i,A,d,f,t):
    if d[i-1]:
        return t
    d[i-1]=t
    t+=1
    for j in A[i-1]:
        t=DFS(j,A,d,f,t)
    f[i-1]=t
    t+=1
    return t

if __name__=="__main__":
    n=int(input())
    A=[]
    for i in range(n):
        A.append(list(map(int,input().split(" ")))[2:])
    d=[0]*n
    f=[0]*n
    t=1
    for i in range(n):
        if d[i]==0:
            t=DFS(i+1,A,d,f,t)
    for i in range(n):
        print("{} {} {}".format(i+1,d[i],f[i]))