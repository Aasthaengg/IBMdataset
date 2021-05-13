# -*- coding: utf-8 -*-
"""
@author: H_Hoshigi
"""
def main():
    N = int(input())
    b_lsit = list(map(int, input().split()))

    flag = True
    answer_list = []
    while flag and b_lsit:
        #print(b_lsit)
        for i in range(len(b_lsit)-1, -2, -1):
            if i == -1:
                flag = False
                break
            elif b_lsit[i] == i+1:
                answer_list.append(b_lsit.pop(i))
                break

    if flag:
        for b in answer_list[::-1]:
            print(b)
    else:
        print(-1)

    return

if __name__ == "__main__":
    main()

