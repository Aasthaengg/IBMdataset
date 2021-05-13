slist = raw_input().split(" ")

new_str_list=[]
for s in slist:
    new_str = ""
    for c in s:
        if c.isupper():
            new_str += c.lower()
        else:
            new_str += c.upper()
    new_str_list.append(new_str)

print " ".join(new_str_list)