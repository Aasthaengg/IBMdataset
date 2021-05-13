L ,R = map(int,input().split())

ans =[]
if R - L <= 2019:
    for i in range(L,R+1):
        for j in range(i+1,R+1):
            ans.append(i*j%2019)

else:
    for i in range(R-L-1010,R-L+1010):
        for j in range(i,R-L+1010):
            ans.append(i*j%2019)

print(min(ans))
