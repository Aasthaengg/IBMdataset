n, k = input().split()
a = int(n)
b = int(k)
s = input()
result = ''
for i in range(a):
    if i == b-1:
        result += chr(ord(s[i]) + 32)
    else:
        result += s[i]
print(result)