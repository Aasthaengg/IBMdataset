N,W=map(int,input().split())
a,b=map(int,input().split())
w0=[b]
w1=[]
w2=[]
w3=[]
for i in range(N-1):
    w,v=map(int,input().split())
    if w-a==0:
        w0.append(v)
    elif w-a==1:
        w1.append(v)
    elif w-a==2:
        w2.append(v)
    else:
        w3.append(v)
w0=sorted(w0,reverse=True)
w1=sorted(w1,reverse=True)
w2=sorted(w2,reverse=True)
w3=sorted(w3,reverse=True)
ans=0
for i in range(max(len(w0)+1,1)):
    for j in range(max(len(w1)+1,1)):
        for k in range(max(len(w2)+1,1)):
            for l in range(max(len(w3)+1,1)):
                if a*i+(a+1)*j+(a+2)*k+(a+3)*l<=W:
                    lst=w0[:i]+w1[:j]+w2[:k]+w3[:l]
                    ans=max(sum(lst),ans)
print(ans)