N = int(input())
A = input()
B = input()
C = input()

ans = 0
for i in range(N):
    temp = [A[i], B[i], C[i]]
    temp = set(temp)
    ans += len(temp)-1
    
print(ans)