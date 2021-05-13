n = int(input())
s = input()
A = []
for i in s:
    A.append(chr(ord(i) + n if ord(i) + n <= 90 else ord(i) + n - 26))
print(''.join(A))