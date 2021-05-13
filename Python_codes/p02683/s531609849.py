def saiki(i,cost,score_list):
   if i == n:
       if min(score_list) >= x:
           ans.append(cost)
   else:
       temp = [score_list[j]+book_list[i][j+1] for j in range(m)]
       saiki(i+1,cost,score_list)
       saiki(i+1,cost+book_list[i][0],temp)

n,m,x = map(int,input().split())
book_list = [list(map(int, input().split())) for _ in range(n)]
ans=[]
saiki(0,0,[0]*m)
print(min(ans) if len(ans)!=0 else -1)