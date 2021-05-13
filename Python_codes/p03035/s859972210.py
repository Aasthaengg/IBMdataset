def main():
    inp=list(map(lambda x:int(x),input().split()))
    A=inp[0]
    B=inp[1]

    res=B
    if A>=6 and A<=12:
        res=res//2
    elif A<=5:
        res=0

    print(res)

if __name__=="__main__":
    main()
    
