s = list(input())
k = int(input())

z = ord("z")
a = ord("a")
for i in range(len(s)-1):
    if s[i] == "a":
        continue
    if z - ord(s[i]) + 1 <= k:
        k -= z - ord(s[i]) + 1
        s[i] = "a"

if k > 0:
    k = k%26
    x = z - ord(s[-1]) +1
    if k >= x:
        k -= z - ord(s[-1]) + 1
        s[-1] = chr(a + k)
    else:
        s[-1] = chr(ord(s[-1])+k)
    
print("".join(s))