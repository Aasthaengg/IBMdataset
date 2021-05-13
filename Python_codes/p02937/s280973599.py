#!/usr/bin/env python3

S = list(input())
T = list(input())

def srch(num,li):
    if len(li)==0:
        return -10

    fst = 0
    lst = len(li)-1
    while(lst>fst):
        mid = (fst+lst)//2
        if li[mid] <= num:
            fst = mid+1
        else:
            lst = mid
    return li[fst]

def main():
    N = len(S)
    li = [[] for _ in range(26)]
    for i in range(N):
        mm = ord(S[i])-97
        li[mm].append(i)
    for i in range(26):
        if len(li[i])>0:
            li[i].append(li[i][0]+N)
    
    cnt1 = 0
    cnt2 = -1
    for i in range(len(T)):
        mm = ord(T[i])-97
        cnt2 = srch(cnt2,li[mm])
        if cnt2 == -10:
            print(-1)
            return

        if cnt2>=N:
            cnt2 %= N
            cnt1 += 1
    print(cnt1*N+cnt2+1)


    

    
        

if __name__ == '__main__':
    main()



