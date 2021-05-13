
N, A, B = map(int,input().split(" "))
ans = 0
diff = abs(A-B)

if diff % 2 == 0:
    ans = diff // 2
else:
    edge = min(A-1, N-B) + 1
    edge += (B-A-1)//2
    ans = edge

print(ans)

