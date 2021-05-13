length=list(map(int,input().split()))
men1 =length[0]*length[1]
men2 =length[2]*length[3]

if men1>=men2:
    print(men1)
else:
    print(men2)