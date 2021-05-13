s = input()

not_ACGT_list = [-1]
max_len = 0

for i in range(len(s)):
    if s[i] != "A" and s[i] != "C" and s[i] != "G" and s[i] != "T":
        not_ACGT_list.append(i)
not_ACGT_list.append(len(s))
#print(not_ACGT_list)
        
for i in range(len(not_ACGT_list)-1):
    max_len = max(max_len,not_ACGT_list[i+1]-not_ACGT_list[i]-1)

print(max_len)