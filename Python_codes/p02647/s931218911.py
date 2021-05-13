# -*- coding: utf-8 -*-
"""
@author: H_Hoshigi
"""

def simulation(N, K, A_list):
    for k in range(min(K, 42)):
        #next_A_list = [0 for i in range(N)]
        imos_list = [0 for i in range(N)]
        for i in range(N):
            d = A_list[i]
            imos_list[max(i-d, 0)] += 1
            if i+d+1 <= N-1:
                imos_list[i+d+1] -= 1
            #for j in range(i-d, i+d+1):
            #    if j >= 0 and j <= N-1:
            #        next_A_list[j] += 1
        for i in range(1, N):
            imos_list[i] += imos_list[i-1]
        A_list = imos_list[:]
        #print(" ".join([ str(i).zfill(2) for i in A_list]))
    return A_list

def main():
    N, K = map(int, input().split())
    A_list = list(map(int, input().split()))
    print(" ".join([ str(i) for i in simulation(N, K, A_list)]))

if __name__ == "__main__":
    main()

