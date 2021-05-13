N,M = map(int,input().split())
*A, = map(int,input().split())
B = sorted((([2,5,5,4,5,6,3,7,6][a-1],a) for a in A),key = lambda x:(x[0],-x[1]))
i = 1
while i<len(B):
    if B[i][0]==B[i-1][0]:
        B.pop(i)
    else:
        i+=1
i = [0]*(len(B)-1)
if len(B)==1:
    print(str(B[0][1])*(N//B[0][0]))
    exit()
ans = []
while i[-1]<B[0][0]:
    tmp = N - sum(j*b[0] for j,b in zip(i,B[1:]))
    if tmp>=0 and tmp%B[0][0] == 0:
        num = ""
        for k,n in sorted(zip([b for _,b in B],[tmp//B[0][0]]+i),key = lambda x:-x[0]):
            num += str(k)*n
        ans.append(int(num))
    i[0]+=1
    for j in range(len(i)-1):
        if i[j]==B[0][0]:
            i[j+1]+=1
            i[j]=0
print(max(ans))