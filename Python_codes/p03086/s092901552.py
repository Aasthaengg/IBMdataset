s =  list(input())
combo = False
cnt = 0
ans = [0,] 
for mozi in s:
    if(mozi == "A" or mozi == "G" or mozi == "C" or mozi == "T"):
        cnt = cnt + 1 
        if combo != True:
            combo = True
    else:
        if combo:
            ans.append(cnt)
            cnt = 0
            combo = False
ans.append(cnt)
print(max(ans))
