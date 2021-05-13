n = int(input())
L = sorted(map(int,input().split()))
ans = 0

if n < 3:
    print(ans)
    exit()

for i in range(n-2):
    for j in range(i+1,n-1):
        for k in range(j+1,n):
            if L[i] != L[j] != L[k]:
                if L[i] + L[j] > L[k]:
                    ans += 1
                    
print(ans)