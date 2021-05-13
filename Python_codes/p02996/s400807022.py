def main():
    n = int(input())
    adic = dict()
    bdic = dict()

    for i in range(n):
        a, b = map(int, input().split())
        adic[i+1] = a
        bdic[i+1] = b
    
    bdic2 = sorted(bdic.items(),key = lambda x:x[1])
    time = 0

    for dic in bdic2:
        shigoto = dic[0]
        time += adic[shigoto]
        if time > dic[1]:
            print("No")
            exit()
    
    print('Yes')





if __name__ == "__main__":
    main()