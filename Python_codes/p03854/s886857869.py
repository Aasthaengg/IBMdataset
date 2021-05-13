s = list(input())
tes = ''
tes2 = ''
tes3 = []
res = 1
tr = -1
for i in range(len(s)) :
    tes += s[i]
    if tes == 'dream' or tes == 'erase' or tes == 'dreamer' or tes == 'eraser' :
        for j in range(i+1,len(s)):
            tes2 += s[j]
            if tes2 == 'dream' or tes2 == 'erase' :
                tr = 1
                #print("TRUE")
                #print(tes2)
                tes2 = ''
                break
            elif len(tes2) >= 7 or j == len(s)-1 :
                tr = 0
                #print("FALSE")
                #print(tes2)
                tes2 = ''
                break
        if tr == 1:
            #print(tes)
            tes3.append(tes)
            tes = ''

            

    elif len(tes) > 7:
        res = 0
        break
        
#print(tes2+'2')
#print(tes3)
#print(tes+'1')
if tes == 'dream' or tes == 'erase' or tes == 'dreamer' or tes == 'eraser':
    tes3.append(tes)
    tes = ''

if  len(tes3) > 0 and len(tes) == 0 :
    print('YES')
else :
    print('NO')