n, k = map(int,input().split())
s = list(map(str,input()))

hp = 0
uhp = 0

for i in range(n-1):
    if s[i] == s[i+1]:
        hp += 1
    else:
        uhp += 1

print(min(n-1,hp+(min(uhp,k))*2))