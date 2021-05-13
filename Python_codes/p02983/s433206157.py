#! python3
#  solve_133C.py

L,R = map(int,input().split())

ans = 3000

for i in range(L,min(R,L+2019)):
    for j in range(i+1,min(R+1,L+2019)):
        ans = min(ans,i*j%2019)
        
print(ans)