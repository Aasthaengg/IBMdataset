import sys
def input(): return sys.stdin.readline().strip()

def main():
    N = int(input())
    A = list(map(int, input().split()))
    d = {1:0, 2:0, 4:0}
    for a in A:
        if a % 2 == 1:
            d[1] += 1
        elif a % 4 == 0:
            d[4] += 1
        else:
            d[2] += 1
    if d[2] == 0 and d[4] + 1 >= d[1]:
        print("Yes")
    elif d[2] != 0 and d[4] >= d[1]:
        print("Yes")
    else:
        print("No")
    

if __name__ == "__main__":
    main()
