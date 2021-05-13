N=int(input())
A=list(map(int, input().split()))
B=list(map(int, input().split()))
if sum(A)<sum(B):
    print(-1)
    exit()

D=[]
X=0
count=0
for i in range(N):
    a=A[i]
    b=B[i]
    if a>b:
        D.append(a-b)
    elif b>a:
        X+=b-a
        count+=1

D=sorted(D, reverse=True)
for d in D:
    if X==0:
        break
    Y=min(d,X)
    X-=Y
    count+=1
    
print(count)