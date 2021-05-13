N = int(input())
S_list = list(input())

ans = ""

# A is 65 in unicode
# Z is 90 in unicode
for i in S_list:
    if 90 < ord(i) + N:
        ans += chr(ord(i) + N - 26)
    else:
        ans += chr(ord(i) + N)

print(ans)
