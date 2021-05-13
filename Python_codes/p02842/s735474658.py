N = int(input())
if (N*100)%108 == 0 :
    print(int(N/1.08))
else :
    for i in range(1,100) :
        if (N*100+i) % 108 == 0 :
            print(int((N*100+i)/108))
            break
    else :
        print(":(")
