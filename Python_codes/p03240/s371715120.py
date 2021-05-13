# -*- coding: utf-8 -*-

def main():
    N  = int(input())
    P = []
    for i in range(N):
        x, y, h = map(int, input().split())
        P.append([h, x, y])
    P.sort(reverse = True)

    for x in range(101):
        for y in range(101):
            distance =abs(x-P[0][1]) + abs(y-P[0][2]) + P[0][0]
            for p in P[1:]:
                if max(distance - abs(x-p[1]) - abs(y-p[2]), 0) !=  p[0]:
                    break
            else:
                print(x, y , distance)
                return

if __name__ == "__main__":
    main()
