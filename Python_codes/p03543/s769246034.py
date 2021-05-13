N = input()
l = len(N)
count = 0
for i in range(l-1):
    if N[i] == N[i+1]:
        count += 1
        if count == 2:
            print('Yes')
            exit()
    else:
        count = 0
print('No')