from collections import defaultdict
def main3():
    N = int(input())
    A = [int(a) for a in input().split()]
    A.sort()

    c = defaultdict(int)
    for a in A:
        c[a] += 1

    if len(c) == 1:
        n = list(c.keys())
        if n[0] == 0:
            print("Yes")
        else:
            print("No")
    
    elif len(c) == 2:
        n = list(c.keys())
        if n[0] == 0 and c[n[1]] == 2*c[n[0]]:
            print("Yes")
        else:
            print("No")
    
    elif len(c) == 3:
        n = list(c.keys())

        if (n[0] ^ n[1] ^ n[2]) == 0 and (c[n[0]] == c[n[1]] == c[n[2]] == N//3):
            print("Yes")
        else:
            print("No")
    else:
        print("No")

if __name__ == "__main__":
    main3()