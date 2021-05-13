S = str(input())
Q = int(input())
Qvery = [0]*Q
for i in range(Q):
    Qvery[i] = list(map(str,input().split()))
frontback = 1
tail = ''
head = ''
for i in range(Q):
    if Qvery[i][0]=='1':
        frontback *= -1
        
    else:
        if Qvery[i][1]=='2':
            if frontback == 1:
                tail +=  str(Qvery[i][2])
            else:
                head = str(Qvery[i][2]) + head
        else:
            if frontback == 1:
                head = str(Qvery[i][2])+head
            else:
                tail += str(Qvery[i][2])
S = head + S + tail
if frontback == -1:
    S = S[::-1]
    
print(S)