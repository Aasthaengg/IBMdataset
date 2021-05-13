s = input()
K = int(input())
alh = [chr(i) for i in range(97, 97 + 26)]
ans = ""
d = {}
for n,i in enumerate(alh):
    d[i] = (26-n)%26
for i in s[:-1]:
    if K >= d[i]:
        K -=d[i]
        ans += "a"
    else:
        ans += i
ans += chr(97+(ord(s[-1])+K-97)%26)
print(ans)