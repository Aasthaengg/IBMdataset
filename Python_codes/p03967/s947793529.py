A= list(input())
p_c = 0
total = 0 
g_c = 0
for i in A:
    if i == "g" and p_c+1 <= g_c:
        total += 1
        p_c += 1
    elif i == "p" and p_c+1 <= g_c:
        p_c += 1
    elif i == "g":
        g_c += 1
    else:
        g_c += 1
        total -= 1
print(total)