s = input()
t = input()
st_dict = {}
flag = True
for i in range(len(s)):
    if s[i] not in st_dict:
        if t[i] in st_dict.values():
            flag = False
            break
        else:
            st_dict[s[i]] = t[i]
            
    else:
        if st_dict[s[i]] != t[i]:
            flag = False
if flag:
    print('Yes')
    
else:
    print('No')