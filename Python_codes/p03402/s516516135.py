a,b=list(map(int,input().split()))
result=['#'*100 for j in range(100)]
for i in range(50):
    result[i]='.'*100
hup=(b-1)//50
hdown=(a-1)//50
wup=(b-1)%50
wdown=(a-1)%50
for i in range(hup):
    result[i*2]='.#'*50
result[hup*2]='.#'*wup+'.'*(100-2*wup)
for i in range(hdown):
    result[i*2+51]='#.'*50
result[hdown*2+51]='#.'*wdown+'#'*(100-2*wdown)
print(100,100)
for i in range(100):
    print(result[i])