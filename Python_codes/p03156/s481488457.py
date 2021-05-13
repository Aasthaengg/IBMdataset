def main():
    N  = int(input())
    A,B  = map(int, input().split()) 
    P = list(map(int, input().split()))  
    c1 = 0
    c2 = 0
    c3 = 0

    for i in range(len(P)):
        if P[i]<=A:
            c1 +=1
        elif P[i]<=B:
            c2 +=1
        else:
            c3 +=1
    print(min([c1,c2,c3]))




if __name__ == '__main__':
    main()
