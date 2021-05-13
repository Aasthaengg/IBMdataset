a = input()
count = [0]*26
ans = 1
for i in range(len(a)):
    x = ord(a[i])-ord("a")
    ans += i-count[x]
    count[x] += 1
print(ans)

