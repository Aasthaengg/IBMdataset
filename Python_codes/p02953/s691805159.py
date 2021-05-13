n = int(input())
h = list(map(int, input().split()))

N=h[0]
for i in range(n):
    if N-1 > h[i]:
        print("No")
        break
    elif h[i] > N:
        N = h[i]
        
else:
    print("Yes")