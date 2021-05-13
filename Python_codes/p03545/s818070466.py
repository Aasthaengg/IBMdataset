abcd=input()

res=''
for i in range(2**3):
    B=format(i,'b').zfill(3)
    sum_=int(abcd[0])
    res=abcd[0]
    j=1
    for k in range(3):
        if B[k]=='1':
            sum_+=int(abcd[j])
            res+='+'
        else:
            sum_-=int(abcd[j])
            res+='-'
        res+=abcd[j]
        j+=1
    if sum_==7:
        break

print('{}=7'.format(res))