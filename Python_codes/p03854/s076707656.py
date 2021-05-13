s=input()
s_re = s[::-1]
list =  ["dream","dreamer","erase", "eraser"]
list_re = [ i[::-1] for i in list]

count=True
while count:
    value=0
    for i in list_re:
        if s_re[:len(i)] == i:
            s_re = s_re[len(i):]
            value=0
        else:
            value+=1
    if value>3:
        count=False

if s_re=="":
    print("YES")
else:
    print("NO")