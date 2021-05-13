from collections import Counter
s = input()
n = len(s)
count = dict(Counter(s))
flag = False

if n ==1:
    flag = True
elif n <= 3:
    if max(count.values())!=2:
        flag = True
elif n==4:
    if max(count.values())<=2:
        flag = True
else:
    if "a" in count:
        if "b" in count:
            if "c" in count:
                if count["a"]==count["b"] or count["b"]==count["c"] or count["c"]==count["a"]:
                    dev = max(count.values())-min(count.values())
                    if dev <= 1:
                        flag = True
            
            
print('YES' if flag==True else 'NO')