n=int(input())
s=[]
s.append(2)
s.append(1)
if n==1:
    print('1')
    exit()
else:
    for i in range(2,87):
        k = s[i-2]+s[i-1]
        s.append(k)
        if i==n:
            print(s[i])
            exit()
