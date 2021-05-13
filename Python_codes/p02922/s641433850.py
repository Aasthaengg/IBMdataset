A,B = map(int,input().split())

if B ==1:
    print(0)
    
else:
    for i in range(1,21):
        N = 1 + A*i -i
        if N >=B:
            print(i)
            break
        else:
            pass