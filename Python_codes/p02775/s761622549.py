def dp_solver(tmp):
    l=len(tmp)
    rev=tmp[::-1]+"0"
    dp=[[float("inf") for _ in range(2)] for _ in range(l+2)]
    dp[0][0]=0
    for i in range(l+1):
        for j in range(2):
            num=int(rev[i])
            num+=j
            if num<10:
                dp[i+1][0]=min(dp[i+1][0],dp[i][j]+num)
            if num>0:
                dp[i+1][1]=min(dp[i+1][1],dp[i][j]+(10-num))

    import numpy as np
    dp=np.array(dp)
    return(dp[l+1])

def y_solver(tmp):
    l=len(tmp)
    rev=tmp[::-1]+"0"
    seq_flag=False
    ans=0
    next_bit=0
    kuri_cal=0
    for i in range(l-1):
        num=int(rev[i])+next_bit
        next_num=int(rev[i+1])
        if not seq_flag:
            if (num<5) or (num==5 and next_num<5):
                ans+=num
                next_bit=0
                kuri_cal=0
                continue
            seq_s=i
            seq_flag=True
            kuri_cal=10-num
            next_bit+=1
            continue
        #print(kuri_cal)
        if num<5:
            ans+=(kuri_cal+num)
            kuri_cal=0
            next_bit=0
            seq_flag=False
        elif num>5:
            kuri_cal+=10-num
        else:
            if next_num<5:
                ans+=(kuri_cal+num)
                next_bit=0
                kuri_cal=0
                seq_flag=False
            else:
                kuri_cal+=10-num
    last=int(tmp[0])+next_bit
    ans+=kuri_cal+min(last,11-last)
    return ans

n=input()
ans=y_solver(n)
print(ans)