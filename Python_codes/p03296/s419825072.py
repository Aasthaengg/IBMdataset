N=int(input())
a=list(map(int,input().split()))
ans=0
x=1#連続して隣り合っている数
for i in range(N-1):
    if i!=(N-2):
        if a[i]==a[i+1]:
            x+=1
        else:
            ans+=(x//2)
            x=1#xをリセット
    else:
        if a[i]==a[i+1]:
            x+=1
        ans+=(x//2)
print(ans)