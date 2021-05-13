N=int(input())
S=list(map(int,input().split()))
count=0
for i in range(N-2):
    if max(S[i],S[i+1],S[i+2])==S[i+1] or min (S[i],S[i+1],S[i+2])==S[i+1]:
        count+=0
    else:
        count+=1
print(count)