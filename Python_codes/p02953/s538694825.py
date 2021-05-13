n = int(input())
H = list(map(int, input().split()))
for i in range(n):
    #print(H)
    if i == 0:
        H[i] -= 1
    else:
        if H[i] < H[i-1]:
            print('No')
            exit()
        elif H[i] == H[i-1]:
            continue
        else:
            H[i] -= 1

#print(H)

for i in range(1, n):
    if H[i] < H[i-1]:
        print('No')
        exit()
else:
    print('Yes')
