#B - Guidebook (別解)
N = int(input())

iSP = []
for i in range(N):
    s,p = input().split()
    iSP.append([i+1,s,int(p)])


ans = sorted(iSP, key = lambda x:x[2], reverse = True)

ans = sorted(ans, key = lambda x:x[1])

for j,k,l in ans:
    print(j)