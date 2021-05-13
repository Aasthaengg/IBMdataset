#!/usr/bin/env python3

N = int(input())
# S = input()
# N, K = map(int, input().split())
A = list(map(int, input().split()))

def main():
    cnt_4 = 0
    cnt_2 = 0
    cnt = 0
    for a in A:
        if a % 4 == 0:
            cnt_4 += 1
        elif a % 2 == 0:
            cnt_2 += 1
        else:
            cnt += 1
    if cnt_4 - cnt >= 0:
        print("Yes")
    elif cnt_4 - cnt == -1:
        if cnt_2 >= 1:
            print("No")
        else:
            print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    main()
