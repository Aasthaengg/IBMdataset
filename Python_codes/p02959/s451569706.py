n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
ans=0
for i in range(n):
    now_a_i=a[i]
    now_b_i=b[i]
    if now_a_i>=now_b_i:
        a[i]=now_a_i-now_b_i
        b[i]=0
        ans+=now_b_i
    else:
        a[i]=0
        b[i]=now_b_i-now_a_i
        ans+=now_a_i
        now_a_i_1=a[i+1]
        now_b_i=b[i]
        if now_a_i_1>=now_b_i:
            a[i+1]=now_a_i_1-now_b_i
            b[i]=0
            ans+=now_b_i
        else:
            a[i+1]=0
            b[i]=now_b_i-now_a_i_1
            ans+=now_a_i_1
print(ans)