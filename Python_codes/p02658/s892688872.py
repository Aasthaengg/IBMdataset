N = int(input())
A = list(map(int,input().split()))
S = 1
if 0 in A:
    print("0")
    exit()
    
for i in range(N):
    S *= A[i]
    if S > 1000000000000000000:
        print("-1")
        exit()

print(S)