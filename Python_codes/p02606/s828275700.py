L,R,d = map(int, input().split())
ans = [int(i) for i in range(L, R+1) if i % d == 0]

print(len(ans))