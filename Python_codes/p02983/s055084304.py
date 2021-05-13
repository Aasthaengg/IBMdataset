L,R = map(int,input().split())

ans = 2018

for i in range(L,min(R,L+2100)):
    for j in range(i+1,min(R+1,i+2100)):
        if (i*j) % 2019 <= ans:
            ans = (i*j) % 2019

print(ans)