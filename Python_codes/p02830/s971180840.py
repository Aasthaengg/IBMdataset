n = int(input())
s,t = map(str, input().split())
w = ""
for i in range(n):
    w += s[i] + t[i]
print(w)