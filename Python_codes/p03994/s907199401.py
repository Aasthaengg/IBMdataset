def str_rotate(S,k): # str_rotate(str,int)
    if k >= 26:
        k = k%26
    if ord(S) + k > 123:
        S = chr(ord(S)+k-97)
    else:
        S = chr(ord(S)+k)
    return S

s = list(input())
k = int(input())
for i in range(len(s)):
    if k == 0:
        break
    if s[i] == "a":
        pass
    elif 123 - ord(s[i]) <= k:
        k -= 123 - ord(s[i])
        s[i] = "a"
    else:
        pass
s[-1] = str_rotate(s[-1],k)
print("".join(s))