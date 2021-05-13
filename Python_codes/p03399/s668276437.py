l=[int(input()) for i in range(4)]
ans_l=[]
for i in range(2):
    for j in range(2,4):
        ans_l.append(l[i]+l[j])
print(min(ans_l))