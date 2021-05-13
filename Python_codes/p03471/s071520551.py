def cal():
    N,Y = map(int,input().split())

    x,y,z = 0,0,0

    an = [-1]*3
    #print(*an)

    for i in range(N+1):
        for j in range(N-i+1):
            if i*10000 + j *5000 +1000*(N - i - j) == Y:
                an[0] = i
                an[1] = j
                an[2] = N-i-j
                print(*an)
                return
    
    print(*an)


if __name__ == "__main__":
    cal()
                
