s = list(input())
n = len(s)
k = int(input())

for i in range(n):
    if k > 0 and i == n-1:
        x = ord(s[i])-ord("a")
        s[i] = chr((k+x)%26+ord("a"))
        break
    if s[i] == "a":
        continue
    x = ord(s[i])-ord("a")

    if k >= 26-x:
        s[i] = "a"
        k -= 26-x
print(*s,sep="")