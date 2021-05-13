
def main():
    H,W,K=map(int,input().split())

    S=[]
    for i in range(H):
        col=list(map(int,list(input())))
        S.append(col)
    CumulativeS=[[S[i][0]] for i in range(H)]
    for i in range(len(S)):
        for j in range(1,len(S[i])):
            CumulativeS[i].append(CumulativeS[i][j-1]+S[i][j])
    for i in range(1,len(S)):
        for j in range(len(S[i])):
            CumulativeS[i][j]+=CumulativeS[i-1][j]
    all_bit=1<<H-1
    res=10000
    for bit in range(all_bit):
        wide_bound=[]
        for i in range(H-1):
            if (bit & (1<<i))!=0:
                wide_bound.append(i)
        res_=len(wide_bound)
        high_bound=[]
        high_flag=0
        for i in range(W):
            if len(high_bound)==0:
                for b in range(len(wide_bound)):
                    if b==0:
                        white_chocolate=CumulativeS[wide_bound[b]][i]
                    else:
                        white_chocolate=CumulativeS[wide_bound[b]][i]-CumulativeS[wide_bound[b-1]][i]

                    if white_chocolate>K:
                        if i-1<0:
                            high_flag=1
                            break
                        high_bound.append(i-1)
                        break
                    if b==len(wide_bound)-1:
                        white_chocolate=CumulativeS[H-1][i]-CumulativeS[wide_bound[b]][i]
                        if white_chocolate > K:
                            if i-1<0:
                                high_flag=1
                                break
                            high_bound.append(i - 1)


                if high_flag==1:
                    break

                if len(wide_bound)==0:
                    white_chocolate = CumulativeS[H - 1][i]
                    if white_chocolate>K:
                        if i-1<0:
                            high_flag=1
                            break
                        high_bound.append(i-1)

            else:
                for b in range(len(wide_bound)):
                    if b == 0:
                        white_chocolate = CumulativeS[wide_bound[b]][i]-CumulativeS[wide_bound[b]][high_bound[len(high_bound)-1]]
                    else:
                        white_chocolate = CumulativeS[wide_bound[b]][i] - CumulativeS[wide_bound[b - 1]][i]-CumulativeS[wide_bound[b]][high_bound[len(high_bound)-1]]+CumulativeS[wide_bound[b-1]][high_bound[len(high_bound)-1]]
                    if white_chocolate>K:
                        if i-1<0:
                            high_flag=1
                            break
                        high_bound.append(i-1)
                        break
                    if b == len(wide_bound) - 1:
                        white_chocolate = CumulativeS[H - 1][i] - CumulativeS[wide_bound[b]][i]-CumulativeS[H-1][high_bound[len(high_bound)-1]]+CumulativeS[wide_bound[b]][high_bound[len(high_bound)-1]]
                        if white_chocolate>K:
                            if i-1<0:
                                high_flag=1
                                break
                            high_bound.append(i-1)

                if high_flag==1:
                    break

                if len(wide_bound)==0:
                    white_chocolate = CumulativeS[H - 1][W - 1]-CumulativeS[H-1][high_bound[len(high_bound)-1]]
                    if white_chocolate>K:
                        if i-1<0:
                            high_flag=1
                            break

                        high_bound.append(i-1)
        res_+=len(high_bound)

        if res_<res and high_flag==0:
            res=res_

    print(res)

if __name__=="__main__":
    main()