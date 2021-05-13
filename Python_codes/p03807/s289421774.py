N = int(input())
A = [int(i) for i in input().split()]

cou = 0
for i in range(N):
    if A[i] % 2 == 1:
        cou += 1
        
if cou % 2 == 0:
    print("YES")
else:
    print("NO")