# B - Five Dishes
C = [int(input()) for _ in range(5)]
C.sort(key=lambda x:-x%10)
ans = 0
for c in C[:4]:
    ans += 10*((c-1)//10+1)
ans += C[4]
print(ans)