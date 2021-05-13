n = int(input())
s = input()
r = 0
b = 0

for i in range(n):
    if s[i] == "B":
        b+=1
    else:
        r+=1
print("Yes" if r>b else "No")
