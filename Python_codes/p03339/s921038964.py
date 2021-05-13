N = int(input())
s = input()
a = [0]*N
for i in range(1,N):
    if s[i]=="E":
        a[0] += 1 
for i in range(1,N):
    a[i] = a[i-1]
    if s[i]=="E":
        a[i] -= 1
    if s[i-1] == "W":
        a[i] += 1
print(min(a))