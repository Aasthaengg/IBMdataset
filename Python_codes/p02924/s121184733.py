# -*- coding: utf-8 -*-
"""
@author: H_Hoshigi
14min 05sec
"""
# 実験したら規則性が見えた。

#import itertools
#
#def test():
#    for i in range(1, ):
#        N = i
#        #N = int(input())
#        N_list = list(range(1, N+1))
#
#        answer = 0
#        for P_list in itertools.permutations(N_list):
#            answer = max(
#                answer,
#                sum([N_list[i] % P_list[i] for i in range(N)])
#            )
#        print(i, answer)

def main():
    N = int(input())
    print(N*(N-1)//2)
    return

if __name__ == "__main__":
    main()


