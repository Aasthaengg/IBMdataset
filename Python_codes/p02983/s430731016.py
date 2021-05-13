L,R = map(int,input().split())

if R-L >= 2100 :
    ans = 0
else :
    ans = 2019
    for i in range(L,R):
        for j in range(i+1,R+1):
            if (i*j)%2019 < ans :
                ans = (i*j)%2019
                if ans == 0 :
                    break

print(ans)
