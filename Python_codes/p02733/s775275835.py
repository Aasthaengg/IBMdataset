    #端から端まで割る
#h<=10に対しては全探索
#wについては極力割らない

h,w,k = map(int, input().split( ))

s= [list(map(int,list(input()))) for i in range(h)]

bit = 1<<h
ans = 10000
for b in range(bit):
    cut = [0]+[j for j in range(1,h) if (b>>j)&1]+[h]
    tmp = len(cut)-2
    white = [0]*h
    for j in range(w):
        for i in range(h): 
            white[i] += (s[i][j])&1
        for u in range(1,len(cut)):
            tmp2 = 0
            for t in range(cut[u-1],cut[u]):
                tmp2 += white[t]
            if tmp2>k and j:##
                tmp += 1
                white = [s[x][j] for x in range(h)]##
            
        for u in range(1,len(cut)):###1列でもアウトな場合
            tmp2 = 0
            for t in range(cut[u-1],cut[u]):
                tmp2 += white[t]
            if tmp2>k and j:##
                tmp = 100000
                white = [s[x][j] for x in range(h)]##
                break##    
    if ans > tmp:
        ans = tmp
print(ans)
        










