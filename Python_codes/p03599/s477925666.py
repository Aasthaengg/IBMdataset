A,B,C,D,E,F=map(int,input().split())

ans=[0,0]
concentration=0.0
for i in range(F//(100*B)+1):
    tmp_water=100*B*i
    for j in range((F-tmp_water)//(100*A)+1):
        tmp_water+=100*A*j
        max_suger=min((tmp_water//100)*E,F-tmp_water)
        for k in range((max_suger)//D+1):
            tmp_suger=D*k
            tmp_suger+=C*((max_suger-tmp_suger)//C)
            if tmp_water+tmp_suger==0:
                continue
            elif tmp_suger/(tmp_water+tmp_suger)>=concentration:
                concentration=tmp_suger/(tmp_water+tmp_suger)
                ans[0]=tmp_water+tmp_suger
                ans[1]=tmp_suger

print(*ans)