#A
a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
k = int(input())

ant = [a,b,c,d,e]
flg = True
for i in range(5):
    for j in range(5):
        if i != j:
            #print(dist)
            dist = abs(ant[i]-ant[j])
            if dist > k:
                flg = False
                break
if flg:
    print('Yay!')
else:
    print(':(')