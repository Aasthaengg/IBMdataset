n = int(input())
s = list(input())
ans = s.count("R")*s.count("G")*s.count("B")
for i in range(n):
    for d in range(n):
        j = i + d
        k = j + d
        if k >= n:
            break
     
        if s[i] != s[j] and  s[i] != s[k] and s[k] != s[j]:
            ans -= 1
print(ans)