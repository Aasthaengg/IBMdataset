# -*- coding: utf-8 -*-
"""
@author: H_Hoshigi
"""
def check_two_str(A, B):
    AtoB_dict = {}
    answer = True
    for i in range(len(A)):
        try:
            AtoB_dict[A[i]]
        except KeyError:
            AtoB_dict[A[i]] = B[i]
        else:
            if AtoB_dict[A[i]] != B[i]:
                answer = False
                break
    return answer

def main():
    S = input()
    T = input()
    if check_two_str(S, T) and check_two_str(T, S):
        print("Yes")
    else:
        print("No")
    return

if __name__ == "__main__":
    main()

