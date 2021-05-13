x = input()
N = int(x)
L = list(map(int,input().split()))
count = 0


for i in range(N-2):
    for j in range(i+1,N-1):
        if L[i] != L[j]:
            for k in range(j+1,N):
                if (L[i] != L[k]) and (L[j] != L[k]) and (L[i] + L[j] > L[k]) and (L[j] + L[k] > L[i]) and (L[k] + L[i] > L[j]):
                    count = count + 1

print(count)