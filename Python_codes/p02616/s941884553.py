# -*- coding: utf-8 -*-
import sys

def main():
    N,K = list(map(int, sys.stdin.readline().split()))
    A_list = list(map(int, sys.stdin.readline().split()))


    A_list.sort(key=lambda x: -abs(x))
    mod = 10**9 + 7

    L_plus  = R_plus  = -1 # the Index of plus value
    L_minus = R_minus = -1 # the Index of minus value
    # L : between index 0 to (K-1)
    # R : between index K to end


    for i in range(K-1, -1, -1):
        if (L_plus == -1) and (A_list[i] >= 0):
            L_plus = i
        if (L_minus == -1) and (A_list[i] < 0):
            L_minus = i
        if (L_plus != -1) and (L_minus != -1):
            break
    
    for i in range(K,N):
        if (R_plus == -1) and (A_list[i] >= 0):
            R_plus = i
        if (R_minus == -1) and (A_list[i] < 0):
            R_minus = i
        if (R_plus != -1) and (R_minus != -1):
            break


    cnt_minus = 0

    for i in range(K):
        if A_list[i] < 0:
            cnt_minus += 1


    if cnt_minus % 2 == 0:
        target_idx = [0, K-1]
    
    else: # cnt_minus % 2 != 0
        if (R_plus == -1) and \
           ( (L_plus == -1) or (R_minus == -1) ) :
        
            calc1 = calc2 = 0
        
        elif (R_plus != -1) and \
           ( (L_plus == -1) or (R_minus == -1) ) :
        
            calc1 = 1
            calc2 = 0
        
        elif (R_plus == -1) and \
           ( (L_plus != -1) and (R_minus != -1) ) :
        
            calc1 = 0
            calc2 = 1
        
        elif (R_plus != -1) and \
           ( (L_plus != -1) and (R_minus != -1) ) :
            
            calc1 = A_list[L_plus] * A_list[R_plus]
            calc2 = A_list[L_minus] * A_list[R_minus]


        if calc1 == calc2:
            target_idx = [N-K, N-1]
        
        elif calc1 > calc2:
            A_list[L_minus], A_list[R_plus] = A_list[R_plus], A_list[L_minus]
            target_idx = [0, K-1]

        elif calc1 < calc2:
            A_list[L_plus], A_list[R_minus] = A_list[R_minus], A_list[L_plus]
            target_idx = [0, K-1]


    ans = 1

    for i in range( target_idx[0], (target_idx[1] + 1) ):
        ans *= A_list[i]
        ans %= mod
    
    print(ans)


if __name__ == "__main__":
    main()
