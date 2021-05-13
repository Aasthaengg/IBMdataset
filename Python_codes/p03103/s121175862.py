N,M = map(int,input().split())
AB_list = []
ans = 0
for i in range(N):
    AB_list.append(list(map(int,input().split())))
AB_list.sort(key = lambda x:x[0])
for i in range(N):
    if(M>=AB_list[i][1]):
        ans += AB_list[i][0]*AB_list[i][1]
        M -= AB_list[i][1]
        if(M==0):
            break
    else:
        ans += AB_list[i][0]*M
        
        break
print(ans)

