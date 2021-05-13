n = int(input())
count = 0

a, b, ab = 0, 0, 0
for _ in range(n):
    s = input()
    if s[-1] == "A" and s[0] == "B":
        ab += 1
    if s[-1] == "A":
        a += 1
    if s[0] == "B":
        b += 1


    for i in range(len(s)-1):
        if s[i:i+2] == "AB":
            count += 1

count += min(a, b)
if max(a, b) == ab and ab != 0:
    count -= 1

print(count)