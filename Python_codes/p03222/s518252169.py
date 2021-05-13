import sys
MOD=10**9+7


h,w,k=map(int,input().split())

dp=[[0]*w for _ in range(h+1)]

dp[0][0]=1

#初期値が0の辞書
zentan1=[0]*(w-1)
zentan2=[0]*(w)

for i in range(2**(w-1)):
    if "11" not in str(bin(i)):
        
        s=(str(bin(i))[2:]).zfill(w-1)
        for index,ss in enumerate(s):        
            #print(index,ss)
            if ss=="1":
                zentan1[index]+=1
            else:
                if index==0:
                    zentan2[index]+=1
                elif index==len(s)-1:
                    zentan2[index+1]+=1
                    if s[index-1]=="0":
                        zentan2[index]+=1
                else:
                    if s[index-1]=="0":
                        zentan2[index]+=1
        #print(zentan1)
        #print(zentan2)






        """
        j=0
        while j<w-1:
            #print(j)
            if i>>j & 1:
                #print(j)
                zentan1[j]+=1
            j+=1
        """

#print("11",zentan1)
#print("00",zentan2)

for i in range(1,h+1):
    x=0
    while x<w:
        for index,mv in enumerate([-1,0,1]):
            if 0<= x+mv < w:
                if index==1:
                    dp[i][x]+=dp[i-1][x+mv]*zentan2[x]
                elif index==0:
                    dp[i][x]+=dp[i-1][x+mv]*zentan1[x-1]
                elif index==2:
                    dp[i][x]+=dp[i-1][x+mv]*zentan1[x]

        x+=1
    #print(dp[i])
print(dp[h][k-1]%MOD)
