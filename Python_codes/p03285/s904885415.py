N = int(input())
ans = 0
for i in range(26):
    for k in range(15):
        if ( 4*i + k*7 ) == N:
            ans = 1
            break
print("Yes" if ans == 1 else "No")
