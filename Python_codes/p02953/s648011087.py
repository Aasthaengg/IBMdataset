N = int(input())
Hs = list(map(int, input().split()))

if(N == 1):
    print("Yes")
    exit()

for i in reversed(range(N - 1)):
    if(Hs[i+1] - Hs[i] >= 0):
        continue

    elif(Hs[i+1] - Hs[i] == -1):
        Hs[i] -= 1
        continue

    else:
#        print(Hs)
        print("No")
        exit()

#print(Hs)
print("Yes")