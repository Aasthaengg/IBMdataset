n = int(input())
s = input()
e_count = [0]*(n+1)
w_count = [0]*(n+1)
for i in range(n):
    if s[i] == "E":
        e_count[i+1] = e_count[i] + 1
        w_count[i+1] = w_count[i]
    else:
        w_count[i+1] = w_count[i] + 1
        e_count[i+1] = e_count[i]
#print(w_count)
#print(e_count)
ans = n+1
for i in range(1, n+1):
    res = 0
    res += w_count[i-1]
    res += e_count[n] - e_count[i]
    ans = min(ans, res)
print(ans)