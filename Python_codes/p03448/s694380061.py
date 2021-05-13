a = int(input())
b = int(input())
c = int(input())
x = int(input())

if x%50 > 0:
    print(0)
    exit()
    
ans = 0
for a_c in range(a+1):
    for b_c in range(b+1):
        amount = 500 * a_c + 100 * b_c
        if 0 <= x - amount <= 50 * c:
            ans += 1

print(ans)