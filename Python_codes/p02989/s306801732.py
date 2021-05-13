N=int(input())
arr=list(map(int,input().split()))

brr=sorted(arr)

if N%2==0:
    ans=brr[int(N//2)]-brr[int(N//2)-1]
else:
    ans=0

print(ans)
