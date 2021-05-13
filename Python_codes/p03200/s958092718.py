

def resolve():
    s=list(input())
    ans=[]
    cnt=0
    for i in s:
        if i=='B':
            cnt+=1
        else:
            ans.append(cnt)
    print(sum(ans))
resolve()