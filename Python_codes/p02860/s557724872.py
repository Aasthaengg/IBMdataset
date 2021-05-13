N = int(input())
S = input()
if(N % 2 == 1):
    print("No")
    exit()
m = N//2
for i in range(m):
    if(S[i] != S[i+m]):
        print("No")
        exit()
print("Yes")