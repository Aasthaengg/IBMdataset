n = int(input())
a = input()
b = input()
c = input()

ans = 0

for i in range(n):
    if a[i] != b[i]:
        ans += 1
    if a[i] != c[i] and b[i] != c[i]:
        ans += 1
        
print(ans)