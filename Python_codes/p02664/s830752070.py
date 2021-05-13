T=input()
T=T.replace('?','D')

cnt=0
before_i=''
for i in list(T):
    if i == 'D':
        cnt+=1
        if before_i=='P':
            cnt+=1
        before_i='D'
    else:
        before_i='P'

print(T)