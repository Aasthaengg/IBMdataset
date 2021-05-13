def main():
    N=int(input())
    A=[int(x) for x in input().split()]
    
    cnt_4=0
    cnt_2=0
    for i in A:
        if i%4==0:
            cnt_4+=1
        elif i%2==0:
            cnt_2+=1
    
    ok=N//2
    if (cnt_4+cnt_2//2)>=ok:
        print("Yes")
    else:
        print("No")
    
if __name__=="__main__":
    main()