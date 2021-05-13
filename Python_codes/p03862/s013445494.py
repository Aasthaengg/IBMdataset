import sys

def resolve():
    readline=sys.stdin.readline
    n,x=map(int, readline().rstrip().split())
    arr=list(map(int, readline().rstrip().split()))
    ans=0
    for i in range(1,len(arr)):
        xx=arr[i-1]+arr[i]
        if xx > x:
            arr[i]-=(xx-x)
            ans+=(xx-x)
            if arr[i]<0:
                arr[i-1]+=arr[i]
                arr[i]=0
    print(ans)
    return

if 'doTest' not in globals():
    resolve()
    sys.exit()