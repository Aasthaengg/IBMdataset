A,B,C = map(int,input().split())

if A+B>=C:
    cnt = B+C
else:
    #Bの分
    cnt = B
    # Cの分
    cnt += A+B
    C -= A+B
    
    cnt += min(1,C)
    
print(cnt)