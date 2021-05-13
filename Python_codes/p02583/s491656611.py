N = int(input())
L = sorted(map(int,input().split()))

cnt = 0

for i in range(N-2):
    a = L[i]
    
    for j in range(i+1,N-1):
        b = L[j]
        if a != b:
            
            for k in range(j+1,N):
                c = L[k]
                if b != c & c != a:
                    if a + b > c:
                        cnt += 1
print(cnt)