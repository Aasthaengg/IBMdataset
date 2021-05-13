#!/usr/bin/env python3

import sys


def main():
    def input(): return sys.stdin.readline().rstrip()
    def ii():    return int(input())
    def isp():   return input().split()
    def mi():    return map(int, input().split())
    def mi_0():  return map(lambda x: int(x)-1, input().split())
    def lmi():   return list(map(int, input().split()))
    def lmi_0(): return list(map(lambda x: int(x)-1, input().split()))
    def li():    return list(input())



    def solve(L):
        M = 0
        command = []
        if L[-1] >= 0:
            # 全て正
            if len(L) > 2:
                command.append([L[-1], L[0]])
                neg = L[-1] - L[0]
                L = L[1:-1]
                for i in range(1, len(L)):
                    command.append([neg, L[i]])
                    neg -= L[i]
                # 最後に正 - 負
                command.append([L[0], neg])
                M = L[0] - neg
            else:
                command.append([L[0], L[1]])
                M = L[0] - L[1]
        elif L[0] <= 0:
            # 全て負
            command.append([L[0], L[-1]])
            pos = L[0] - L[-1]            
            L = L[1:-1]
            for i in range(len(L)):
                command.append([pos, L[i]])
                pos -= L[i]
            M = pos
        else:
            for i in range(len(L)):
                if L[i] < 0:
                    break
            neg = L[i]
            for j in range(1, i):
                command.append([neg, L[j]])
                neg -= L[j]
            L = [L[0], neg] + L[i+1:]
            M = L[0]
            for i in range(1, len(L)):
                command.append([M, L[i]])
                M -= L[i]
        return M, command
                

    
    
    n = ii()
    L = lmi()
    L.sort(reverse=True)
    M, command = solve(L)
    print(M)
    for x, y in command:
        print(f"{x} {y}")


if __name__ == "__main__":
    main()
