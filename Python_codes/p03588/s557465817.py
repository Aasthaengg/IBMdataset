A_B=[list(map(int,input().split())) for _ in range(int(input()))]
ans=[A_B[0][0],A_B[0][1]]
for a_b in A_B:
    if ans[0]<a_b[0]:
        ans[0]=a_b[0]
    if ans[1]>a_b[1]:
        ans[1]=a_b[1]
print(sum(ans))