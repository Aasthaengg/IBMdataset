n = int(input())

out = ""
while n > 0:
    n -= 1
    out += chr(ord('a') + n % 26)
    n //= 26

print(out[::-1])