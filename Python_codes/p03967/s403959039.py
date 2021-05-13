s = input()

g_cnt=0
for te in s:
    if te=="g":
        g_cnt+=1
p_cnt=len(s)-g_cnt
best_p=len(s)//2
diff = best_p - p_cnt
print(diff)