x= input()
l_w = []
for i in range(len(x)):
    if x[i] == 'W':
        l_w.append(i)
#print(l_w)
sum = 0
st = 0
for i,j in enumerate(l_w):
    sum += j-st
    st+= 1
print(sum)