n = int(input())
s = str(input())
s = s.replace("W","1")
s = s.replace("E","0")
fl = sum(list(map(int,s)))
k = 0
p = 0
for i in range(n):
    if i == 0:
        p = fl - int(s[0])
        k = p
    elif i == n-1:
        p = n-1-fl+int(s[n-1])
        if p > k:
            k = p
    else:
        if (s[i-1] == "1" and s[i] == "1"):
            p -= 1
        elif (s[i-1] == "1" and s[i] == "0"):
            continue
        elif (s[i-1] == "0" and s[i] == "1"):
            continue
        else:
            p += 1
            if p > k:
                k = p
print(n-k-1)