import sys
def input(): return sys.stdin.readline().strip()


def main():
    C = [list(map(int, input().split())) for _ in range(3)]
    rumor = True
    for i in range(1, 3):
        diff1 = C[i][0] - C[0][0]
        diff2 = C[i][1] - C[0][1]
        diff3 = C[i][2] - C[0][2]
        if diff1 != diff2 or diff2 != diff3 or diff1 != diff3:
            rumor = False
            break
    if rumor: print("Yes")
    else: print("No")

if __name__ == "__main__":
    main()
