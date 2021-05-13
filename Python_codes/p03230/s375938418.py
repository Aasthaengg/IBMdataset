N=int(input())

L=[]
for i in range(1,10**5):
    if (i*(i+1)//2)>10**5:
        break
    else:
        L.append(i*(i+1)//2)
#print(i)
if N not in L:
    print("No")
    exit()
print("Yes")
for i in range(448):
    if N==i*(i+1)//2:
        print(i+1)
        break
L=[i+1 for i in range(i)]
ans=str(i)
for j in L:
    ans+=" "+str(j)
print(ans)
A=[[a+1]for a in range(i)]
#print(A)
cnt=i+1
for a in range(1,i+1):
    for b in range(i):
        if cnt>(((i)*(i+1))//2):
            break
        A[b%(i)].append(cnt)
        A[(b+a)%(i)].append(cnt)
        cnt+=1
#print(A)
for a in range(i):
    ANS=str(i)
    for j in A[a]:
        ANS+=" "+str(j)
    print(ANS)