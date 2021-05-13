n = int(input())
s = input()
c_r = 0
c_g = 0
c_b = 0
for i in range(n):
    if s[i] == "R":
        c_r += 1
    elif s[i] == "G":
        c_g += 1
    elif s[i] == "B":
        c_b += 1
c = 0
for i in range(n-2):
    for j in range(i+1,n-1):
        if s[i] == "R" and s[j] == "G":
            if j < 2*j-i < n:
                if s[2*j-i] == "B":
                    c += 1
        if s[i] == "R" and s[j] == "B":
            if j < 2*j-i < n:
                if s[2*j-i] == "G":
                    c += 1
        if s[i] == "G" and s[j] == "R":
            if j < 2*j-i < n:
                if s[2*j-i] == "B":
                    c += 1
        if s[i] == "G" and s[j] == "B":
            if j < 2*j-i < n:
                if s[2*j-i] == "R":
                    c += 1
        if s[i] == "B" and s[j] == "R":
            if j < 2*j-i < n:
                if s[2*j-i] == "G":
                    c += 1
        if s[i] == "B" and s[j] == "G":
            if j < 2*j-i < n:
                if s[2*j-i] == "R":
                    c += 1
        else:
            pass
print(c_r*c_g*c_b-c)