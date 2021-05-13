s=list(list(input())[::-1])
t=list(list(input())[::-1])
s_len=len(s)
t_len=len(t)
for i in range(s_len-t_len+1):
    for j in range(t_len):
        if s[i+j]!="?" and t[j]!=s[i+j]:
            break
    else:
        s[i:i+t_len]=t 
        for k in range(s_len):
            if s[k]=="?":
                s[k]="a"
        print("".join(s[::-1]))
        exit()
print("UNRESTORABLE")