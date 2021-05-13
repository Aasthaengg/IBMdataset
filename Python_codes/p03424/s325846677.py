N=int(input())
S=list(map(str,input().split()))
S=set(S)
if len(S)==3:
    ans="Three"
elif len(S)==4:
    ans="Four"
print(ans)