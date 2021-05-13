s=input()
l = [0]
cnt = 0
for i in s:
    if i =='A'or i == 'C' or i == 'G' or i == 'T':
        cnt +=1
        l.append(cnt)
    else:
        cnt = 0
print(max(l))