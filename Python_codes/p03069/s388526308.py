# -*- coding: utf-8 -*-
"""
@author: H_Hoshigi
解説PDFを読んだ。
"""

def main():
    N = int(input())
    S = input()

    hash_counter = 0
    dot_counter = S.count(".")
    answer = dot_counter
    for i in range(N):
        if S[i] == "#":
            hash_counter += 1
        else:
            dot_counter -= 1
        answer = min(answer, hash_counter+dot_counter)
    print(answer)

if __name__ == "__main__":
    main()

