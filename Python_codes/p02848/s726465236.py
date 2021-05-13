n = int(input())
s = input()
ans = [chr(ord(s_)+n) if (ord(s_)+n)<91 else chr((ord(s_)+n)-26) for s_ in s ]
print(''.join(ans))