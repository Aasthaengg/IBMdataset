A,B,C= map(int,input().split())

cnt = 0
if A%2==1 or B%2==1 or C%2==1:
    print(cnt)
elif A==B==C:
    print('-1')
else:
    flag = True
    while flag:
        A, B, C = (B+C)//2, (A+C)//2, (A+B)//2
        cnt += 1
        if A%2==0 and B%2==0 and C%2==0:    
            continue
        else:
            flag = False

    print(cnt)