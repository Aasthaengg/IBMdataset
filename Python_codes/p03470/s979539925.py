N = int(input())
ans = 0
D=[]
for i in range(N):
    D.append(int(input()))
num=[0]*110
for i in range(N):
    #print(D[i])
    num[D[i]]+= 1
    #print(num[D[i]])
for i in range(110):
    if num[i] > 0:
        ans += 1
print(ans)