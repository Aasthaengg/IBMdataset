N = int(input())
F = [int(x) for x in input().split()]

flag = True
for i in range(N-1):
    if F[i] < F[i+1]:
        F[i+1] -= 1
    elif F[i] > F[i+1]:
        flag = False
        break
    
if flag == True:
    print("Yes")
else:print("No")