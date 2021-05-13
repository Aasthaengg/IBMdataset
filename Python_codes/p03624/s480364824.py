S=set(list(input()))
l=[chr(i+97)for i in range(26)if not chr(i+97)in S]
print(l[0]if len(l)else'None')