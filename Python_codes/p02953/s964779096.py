N = int(input())
H = list(map(int,input().split()))

for i in range(N-1,0,-1):
    if H[i-1] - H[i] > 1:
        print("No")
        exit()
    if H[i-1] - H[i] == 1:
        H[i-1] -= 1

for i in range(N-1):
    if H[i] > H[i+1]:
        print("No1")
        exit()
        
print("Yes")