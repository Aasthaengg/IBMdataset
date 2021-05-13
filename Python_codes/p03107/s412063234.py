S = input()

s0 = 0
s1 = 0
for i in S:
    if i == "0":
        s0 += 1
    elif i == "1":
        s1 += 1
    
print(min(s0, s1) * 2)