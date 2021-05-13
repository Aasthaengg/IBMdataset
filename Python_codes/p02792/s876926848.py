n=int(input())
D=[[0 for _ in range(10)] for _ in range(10)]
for i in range(1,n+1):
    s=str(i)
    D[int(s[0])][int(s[-1])]+=1
a=0
for i in range(10):
    for j in range(10):
        a+=D[i][j]*D[j][i]
print(a)