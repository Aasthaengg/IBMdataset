L = list(map(int, input().split()))

ans1 = L[0]*L[1]*(L[2]//2-(L[2]-L[2]//2))
ans2 = L[0]*L[2]*(L[1]//2-(L[1]-L[1]//2))
ans3 = L[1]*L[2]*(L[0]//2-(L[0]-L[0]//2))
print(min(abs(ans1), abs(ans2), abs(ans3)))
