N = int(input())
A_s = list(map(int, input().split()))

if (N % 2 == 0):
    FLAG = True
else:
    FLAG = False

even = A_s[1::2]
odd = A_s[0::2]
ans = []


if (FLAG):
    even = even[::-1]
    even.extend(odd)
    ans = even
    
else:
    odd = odd[::-1]
    odd.extend(even)
    ans = odd

ans = map(str, ans)

print(' '.join(ans))