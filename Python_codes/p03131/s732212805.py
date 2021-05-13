K, A, B = map(int, input().split())

if B-1 <= A:
    print(K+1)
    exit()

count = max(0, (K - (A-1))//2)
ans = (K+1) - 2*count + (B-A)*count
print(ans)
