N=int(input())
stock=[N-i for i in range(N)]

"""
if N==2:
    print("Yes")
    print(2)
    print(2,1,2)
    print(2,1,2)
    exit()
"""

N*=2
n=-int(-N**0.5//1)
if N/n==N//n and (n-N//n)==1:
    yoko=N//n
else:
    print("No")
    exit()

ans=[[0 for j in range(yoko)]for i in range(n)]

for i in range(N-1):
    for j in range(i,yoko):
        temp=stock.pop(-1)
        ans[i][j]=temp
        ans[j+1][i]=temp

print("Yes")
print(len(ans))
for item in ans:
    print(len(item), *item)
