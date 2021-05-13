num = input()
ans = 0

while num > 0:
    if num%10 == 2:
        ans += 1
    num /= 10

print ans