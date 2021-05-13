a = int(input())
b = int(input())
c = int(input())
x = int(input())
ans = 0
ab = 0
for a_count in range(a + 1):
    for b_count in range(b + 1):
        ab = a_count * 500 + b_count * 100
        if ab <= x <= (ab + c * 50):
            ans += 1
print(ans)
