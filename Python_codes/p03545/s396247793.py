def dfs(i,sumnum,sums):
    global ans
    if i == 4:
        if sumnum == 7:
            print(sums + "=7")
            exit()
    else:
        dfs(i+1,sumnum + int(s[i]),sums + "+" + s[i])
        dfs(i+1,sumnum - int(s[i]),sums + "-" + s[i])
s = input()
dfs(1,int(s[0]),s[0])
