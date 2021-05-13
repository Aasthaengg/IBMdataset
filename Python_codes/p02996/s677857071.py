N=int(input())
AB=[]
for i in range(N):
    ab=list(map(int,input().split()))
    AB.append(ab)

AB.sort(key=lambda x:x[1])

ans="Yes"
sum_A=0
for i in range(N):
    sum_A+=AB[i][0]

    if sum_A>AB[i][1]:
        ans="No"
        break

print(ans)