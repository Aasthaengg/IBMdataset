from sys import exit
 
N = int(input())
h = list(map(int,input().split()))

for i in range(N-1,0,-1):
    if h[i] < h[i-1]:
        h[i-1] -= 1
    
    if h[i] < h[i-1]:
        print("No")
        exit(0)

print("Yes")