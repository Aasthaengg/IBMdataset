def main2():
    N=int(input())
    #各交通機関の移動人数
    t=[int(input()) for _ in range(5)]
    MIN=min(t)
    if N%MIN==0:
        m=N//MIN+4
    else:
        m=N//MIN+1+4
    print(m)

if __name__=="__main__":
    main2()