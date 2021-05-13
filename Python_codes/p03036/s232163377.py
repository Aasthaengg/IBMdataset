def main():
    inp=list(map(lambda x:int(x),input().split()))
    r=inp[0]
    D=inp[1]
    x=inp[2]

    res_array=[]
    for i in range(10):
        x=r*x-D
        res_array.append(x)

    for i in res_array:
        print(i)


if __name__=="__main__":
    main()
    

    
