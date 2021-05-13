N,M=map(int,input().split())
H=list(map(int,input().split()))
AB=[]
ans = [True]*N
for i in range(M):
    ls1=list(map(int,input().split()))
    AB.append(list(ls1))
    ls1.clear()
    #print(AB)
    if H[AB[i][0]-1] <= H[AB[i][1]-1]:
        ans[AB[i][0]-1] = False
    if H[AB[i][0]-1] >= H[AB[i][1]-1]:
        ans[AB[i][1]-1] = False
print(sum(ans))
