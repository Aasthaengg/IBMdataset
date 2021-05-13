C=[list(map(int,input().split()))for _ in range(3)]
ans='Yes'

if C[1][0]-C[0][0]!=C[1][1]-C[0][1]:
    ans='No'
elif C[1][2]-C[0][2]!=C[1][1]-C[0][1]:
    ans='No'
elif C[2][0]-C[1][0]!=C[2][1]-C[1][1]:
    ans='No'
elif C[2][2]-C[1][2]!=C[2][1]-C[1][1]:
    ans='No'

print(ans)