n = int(input())
s = input()
a = ""
for ss in s:
    if ord('A') <= ord(ss) + n <= ord('Z'):
        a += chr(ord(ss) + n)
    else:
        a += chr(ord(ss) + n - ord('Z') + ord('A') - 1)
print(a)
