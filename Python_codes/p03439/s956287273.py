def main():
    N=int(input())
    ans = [None]*N
    
    print(0)
    s=input()
    if s=="Vacant":return
    ans[0] = s=="Male"
    l=1
    r=N-1
    while l+1<r:
        i = (l+r)//2
        print(i)
        s=input()
        if s=="Vacant":return
        ans[i] = s=="Male"
        if (ans[i]==ans[0]) ^ (i%2!=0):
            l = i
        else:
            r = i
    print(l)
    s=input()
    if s=="Vacant":return
    print(r)
    return

main()