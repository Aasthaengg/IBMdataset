n = int(input())
H = list(map(int,input().split()))


#print(H)

flag = True

for i in range(n-1):
    if H[i+1] > H[i]:
        H[i+1] -= 1
    
    if H[i+1] < H[i]:
        flag = False
        break

if flag:
    print("Yes")
else:
    print("No")