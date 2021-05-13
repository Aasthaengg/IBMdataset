n = int(input())
s = input()
t = input()
ans = 2*n
for i in range(n):
    check = True
    for j in range(n-i):
        if s[i+j] != t[j]:
            check = False
            break
    if check:
        ans = min(ans,i+n)
print(ans)