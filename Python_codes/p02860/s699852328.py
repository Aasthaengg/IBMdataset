N = int(input())
S = list(input())

if N % 2 != 0:
    print('No')
    exit()

for i in range(N//2):
    if S[i] == S[i + (N//2)]:
        continue
    else:
        print('No')
        exit()
        
print('Yes')