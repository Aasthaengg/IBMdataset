N = int(input())
S = input()
ans = ""
for i in S:
    if (ord(i)+N) >= 91:
        ans += chr(ord(i)+N-26)
    else:
        ans += chr(ord(i)+N)
print(ans)
