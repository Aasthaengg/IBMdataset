
n = int(input())

alphabet = [chr(i) for i in range(ord('a'), ord('z')+1)]

ans = ''
while n > 0:
    n -= 1
    ans += alphabet[n%26]
    n = n//26

print(ans[::-1])
