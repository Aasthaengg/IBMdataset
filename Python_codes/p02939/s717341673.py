s = input()
i = 0
s_list = [""]
for j in range(1,len(s)+1):
    if s[i:j] != "" and s[i:j] != s_list[-1]:
        s_list.append(s[i:j])
        i = j
print(len(s_list)-1)