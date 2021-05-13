n=int(input())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
if sum(A)>sum(B):
    ans='No'
else:
    l=sum(B)-sum(A)
    cnt_a=l*2
    cnt_b=l
    for i in range(n):
        if A[i]>B[i]:
                cnt_b-=(A[i]-B[i])
        else:
            if (B[i]-A[i])%2==0:
                cnt_a-=(B[i]-A[i])
            else:
                cnt_a-=(B[i]-A[i])+1
                cnt_b-=1
    if cnt_a==cnt_b and cnt_a>=0:
        ans='Yes'
    else:
        ans='No'
print(ans)