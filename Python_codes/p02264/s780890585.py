#coding:UTF-8
def Queue(n,q,B):
    ans=[]
    ftime=0
    while len(B)>0:
        name=B[0].split(" ")[0]
        time=int(B[0].split(" ")[1])
        if time>q:
            ftime+=q
            newB=name+" "+str(time-q)
            B.append(newB)
            B.pop(0)
        else :
            ans.append(name+" "+str(ftime+time))
            B.pop(0)
            ftime+=time
    for i in range(n): 
        print(ans[i])
        
  
if __name__=="__main__":
    a=input()
    n=int(a.split(" ")[0])
    q=int(a.split(" ")[1])
    B=[]
    for i in range(n):
        B.append(input())
    Queue(n,q,B)