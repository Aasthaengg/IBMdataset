# AtCoder Beginners Selection Otoshidama
import math

N,Money = map(int, input().split())
if(1000*N<=Money<10000*N):
    tenthousand_list=[num for num in range(0,Money+1,10000)]
    fivethousand_list=[num for num in range(0,Money+1,5000)]
    possible_tenthousand=math.floor(Money/10000)
    while (possible_tenthousand >=0):
        ##残り金額と残り枚数を計算
        zan_number=N-possible_tenthousand
        zan_Money=(Money-tenthousand_list[possible_tenthousand])
        if(5000*zan_number>=zan_Money):
            possible_fivethousand=math.floor(zan_Money/5000)
            while (possible_fivethousand>=0):
            
                if(tenthousand_list[possible_tenthousand]+fivethousand_list[possible_fivethousand]+
                   (1000*(N-possible_tenthousand-possible_fivethousand))==Money):
                    zan_Money=0
                    break
                else:
                    possible_fivethousand-=1
        else:
            print("-1 -1 -1")
            break
        
        if((zan_Money==0) and (possible_fivethousand!=-1) ):
            print(str(possible_tenthousand) + " " + str(possible_fivethousand)+ " " + str(N-possible_tenthousand-possible_fivethousand) )
            break

            
        possible_tenthousand-=1

        
        if(possible_fivethousand==-1 and possible_tenthousand ==-1):
            print("-1 -1 -1")
            break
        

        
elif(Money==10000*N):
    print(str(N) + " 0 "+ "0") 

else:
    print("-1 -1 -1")




