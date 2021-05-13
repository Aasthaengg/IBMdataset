s = input()
p_cnt=0
for te in s:
    if te=="p":
        p_cnt+=1
best_p=len(s)//2
diff = best_p - p_cnt
print(diff)