n = int(input())
alpha = "abcdefghijklmnopqrstuvwxyz"
ans = ""
counter = 0
while n!=0:
    n -= 1
    ans += alpha[n%26]
    n //= 26
print(ans[::-1])
