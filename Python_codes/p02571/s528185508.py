s = input()
t = input()

ans = len(t)
long = ans

for i in range(len(s)+1-long):
    count = 0
    for j in range(long):
        if s[i+j] != t[j]:
            count += 1
    if count < ans:
        ans = count

print(ans)