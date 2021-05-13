#!/usr/bin/env python3

def main():
    N = int(input())
    A = list(map(int,input().split()))
    A.sort()

    li = []
    mm1 = A[N-1]
    mm2 = A[0]
    i = 1
    while(i<N-1):
        if A[i]<=0:
            li.append([mm1,A[i]])
            mm1 -= A[i]
        else:
            li.append([mm2,A[i]])
            mm2 -= A[i]
        i += 1
    li.append([mm1,mm2])
    print(mm1-mm2)
    for i in range(N-1):
        print(*li[i])
    

        


if __name__ == '__main__':
    main()



