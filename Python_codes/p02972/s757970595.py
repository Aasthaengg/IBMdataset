n = int(input())
A = list(map(int, input().split()))
 
B = [0]*n
ans = []
 
for i in range(n-1,-1,-1):
    if sum(B[i::i+1])%2!=A[i]:
        B[i] = 1
        ans.append(i+1)
print(len(ans))
print(*ans)