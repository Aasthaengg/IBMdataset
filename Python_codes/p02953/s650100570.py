n = int(input())
H = list(map(int, input().split()))[::-1]
ok = True
for i in range(n-1):
    if H[i] >= H[i+1]: continue
    if H[i] >= H[i+1]-1:
        H[i+1] -= 1
    else:
        ok = False
        break
print("Yes" if ok else "No")