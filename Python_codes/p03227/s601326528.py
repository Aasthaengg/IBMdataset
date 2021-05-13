a=list(input())
if len(a)==3:
    a.reverse()
    ans=""
    for i in a:
        ans+=i
    print(ans)
elif len(a)==2:
    ans = ""
    for i in a:
        ans += i
    print(ans)