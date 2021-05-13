import sys
import math

input = sys.stdin.readline

def main():
    N, H = map(int, input().split())
    katana = []
    for _ in range(N):
        a, b = map(int, input().split())
        katana.append([a, 1])
        katana.append([b, 0])
    
    katana.sort(key=lambda x: x[0])
    nage = 0; ans = 0
    while True:
        tmp = katana.pop()
        nage += tmp[0]*(tmp[1] == 0)
        ans += (tmp[1] == 0)
        if nage >= H:
            print(ans)
            return
        if tmp[1] == 1:
            attack = tmp[0]
            break

    ans += math.ceil((H - nage)/attack)
    print(ans)

if __name__ == "__main__":
    main()
