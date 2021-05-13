S = input()
K = int(input())

if S==S[0]*len(S):
    print(len(S)*K//2)
    exit()
    
rle = []
cnt = 1

for i in range(len(S)-1):
    if S[i]!=S[i+1]:
        rle.append((S[i], cnt))
        cnt = 1
    else:
        cnt += 1

rle.append((S[-1], cnt))
#print(rle)

if rle[0][0]==rle[-1][0]:
    ans = rle[0][1]//2+rle[-1][1]//2
    
    for i in range(1, len(rle)-1):
        ans += rle[i][1]//2*K
    
    ans += (rle[0][1]+rle[-1][1])//2*(K-1)
else:
    ans = 0
    
    for i in range(len(rle)):
        ans += rle[i][1]//2*K
    
print(ans)