n = int(input())
H = list(map(int,input().split()))

h_max = 0
for i in range(len(H)):
    if i == 0:
        h_max = H[i]
    else:
        if h_max <= H[i]+1:
            if h_max < H[i]:
                h_max = H[i]
        else:
            print ("No")
            exit ()

print ("Yes")
