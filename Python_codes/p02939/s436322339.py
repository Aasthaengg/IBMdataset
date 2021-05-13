S = input()
li = []
st = ''
for c in S:
    st += c
    if len(li) == 0:
        li.append(st)
        st = ''
    elif li[len(li) - 1] == st:
        continue
    else:
        li.append(st)
        st = ''
print(len(li))