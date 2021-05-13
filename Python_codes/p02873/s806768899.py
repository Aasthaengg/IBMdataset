s = input()
s_len = len(s)
li = [0]*(s_len+1)
for i in range(0,s_len):
    if s[i] == "<":
        if li[i] >= li[i+1]:
            li[i+1] = li[i] + 1
for i in range(s_len-1,-1,-1):
    if s[i] == ">":
        if li[i] <= li[i+1]:
            li[i] = li[i+1]+1
print(sum(li))