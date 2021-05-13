def f():
    n,k=map(int,input().split())
    s=input()

    ans=0
    pre="1"
    right,SUM=0,0
    for left in range(n):
        while right<n and SUM+int(pre=="1" and s[right]=="0")<=k:
            SUM+=int(pre=="1" and s[right]=="0")
            pre=s[right]
            right+=1

        while right<n and s[right]=="1":
            right+=1
        if ans<max(ans,right-left):
            ans=right-left

        if right==left:right+=1;pre="1"
        elif left<n-1:SUM-=int(s[left]=="0"and s[left+1]=="1")
    print(ans)
if __name__ == "__main__":
    f()