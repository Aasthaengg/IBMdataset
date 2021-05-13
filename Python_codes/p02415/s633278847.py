S = input()
ans = ""
for i in range(len(S)):
    if 97<=ord(S[i])<=122:
        ans += chr(65+int(ord(S[i]))-97)
    elif 65<=ord(S[i])<=90:
        ans += chr(97+int(ord(S[i]))-65)
    else:
        ans += S[i]
print(ans)
