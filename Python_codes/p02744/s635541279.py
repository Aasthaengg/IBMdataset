def dfs(i,sent):
    if len(sent)==N:
        print(sent)
        return
    if i>N:
        return
    for j in range(i+1):
        dfs(max(i,j+1),sent+chara[j])
    return

N=int(input())
chara=["a","b","c","d","e","f","g","h","i","j"]
chara=chara[:N]
ans=[]
dfs(1,"a")