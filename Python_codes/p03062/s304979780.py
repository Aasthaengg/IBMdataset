N = int(input())
A = list(map(int, input().split()))
S = sum(map(abs, A))
 
cnt = 0
 
for a in A:
    if a > 0:
        cnt += 1
        
if (len(A)-cnt)%2==0 or 0 in A:
    print(S)
else:
    print(S-2*min(map(abs, A)))