N, A, B, C, D = map(int, input().split())
S = input()

for i in range(A, max(C, D)):
    if S[i-1:i+1] == '##':
        print('No')
        exit(0)

if C < D:
    print('Yes')
    exit(0)

for i in range(B-1, D):
    if S[i-1:i+2] == '...':
        print('Yes')
        exit(0)
print('No')
