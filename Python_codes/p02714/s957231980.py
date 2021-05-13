n = int(input())
s = input()
r,g,b = 0,0,0
for i in s:
    if i == "R":
        r += 1
    elif i == "G":
        g += 1
    else:
        b += 1
ans_1 = r * g * b
ans_2 = 0
for i in range(n):
    for j in range(i+1,n):
        if s[i] == s[j]:
            continue
        k = j - i + j
        if k >= n or s[k] == s[i] or s[k] == s[j]:
            continue
        #print(i,j,k)
        ans_2 += 1

print(ans_1-ans_2)
