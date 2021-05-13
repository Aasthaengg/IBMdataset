n = input()
s = list(input())
n = int(n)

r = s.count("R")
g = s.count("G")
b = s.count("B")
ans = r*g*b

for i in range(1,n):
    for j in range(min(i+1,n-i)):
        k = j*2 -i
        if j - i == k -j:
            if k <= n and s[i] != s[i+j] and s[i] != s[i-j] and s[i+j] != s[i-j]:
                ans -= 1
print(ans)