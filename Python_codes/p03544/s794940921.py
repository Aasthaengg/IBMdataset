if __name__ == '__main__':
    n = int(input())
    list =[0]*86
    list[0]=2
    list[1]=1

    for i in range(2,86):
        list[i]=list[i-1]+list[i-2]

    if n ==86:
        print("939587134549734843")
    else:
        print(list[n])