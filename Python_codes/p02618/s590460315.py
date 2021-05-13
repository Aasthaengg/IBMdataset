def AtCoderContestScheduling():

    Day = int(input())
    C_i = list(map(int,input().split()))
    
    last_d_i = [0]*26

    SatisfactionLevel_last = 0

    for num in range(1, Day+1):
        
        S_d_i = list(map(int,input().split()))
        
        SatisfactionLevel_list = []
        
        for num2 in range(26):
            SatisfactionLevel = SatisfactionLevel_last + S_d_i[num2]
            
            for num3 in range(26):
                if num2 != num3:
                    SatisfactionLevel = SatisfactionLevel - C_i[num3]*(num - last_d_i[num3])
 
            SatisfactionLevel_list.append(SatisfactionLevel)    

        index = SatisfactionLevel_list.index(max(SatisfactionLevel_list))

        last_d_i[index] = num

        SatisfactionLevel_last = SatisfactionLevel_list[SatisfactionLevel_list.index(max(SatisfactionLevel_list))]

        print(SatisfactionLevel_list.index(max(SatisfactionLevel_list)) + 1)

if __name__ == '__main__':
    AtCoderContestScheduling()



