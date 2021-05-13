A,B =map(int,input().split())
flg = False
for i in range(1,1009):
    if int(i*8/100) == A and int(i/10) == B:
        print(i)
        flg = True
        break
if flg == False:
    print(-1)
