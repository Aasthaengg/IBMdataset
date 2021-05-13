def dsf(i,sum1,ans):
    if i == 4:
        if ans == 7:
            print(sum1 + "=7")
            exit()
    else:
        dsf(i+1,sum1+"+"+abcd[i],ans + int(abcd[i]))
        dsf(i+1,sum1+"-"+abcd[i],ans - int(abcd[i]))


abcd = input()
dsf(1,abcd[0],int(abcd[0]))