s = list(input())
k = int(input())
n = len(s)
al=[chr(ord('a') + i) for i in range(26)]

for i in range(n):
    now = ord(s[i]) - ord('a')
    if now != 0:
        if k >= 26 - now:
            s[i] = "a"
            k -= 26 - now
        
s[n-1] = al[(ord(s[n-1])-ord("a") + k) % 26]

for i in s:
    print(i,end="")