def main():
    import sys
    input = sys.stdin.readline
    A, B, C, D, E, F = map(int, input().split())
    waters = set()
    for i in range(0, F, A):
        for j in range(0, F, B):
            ij = i * 100 + j * 100
            if ij > F:
                break
            waters.add(ij)
    sugers = set()
    for i in range(0, F, C):
        for j in range(0, F, D):
            ij = i + j
            if ij > F:
                break
            sugers.add(ij)
    ans_water = 0
    ans_suger = 0
    ans = 0
    for water in waters:
        for suger in sugers:
            if water + suger == 0:
                continue
            if water + suger > F:
                continue
            if 100 * suger > E * water:
                continue
            if 100 * suger / (water + suger) > ans:
                ans = 100 * suger / (water + suger)
                ans_water = water
                ans_suger = suger
    if ans_suger == 0:
        if A * 100 <= F:
            print(A*100, 0)
        elif B * 100 <= F:
            print(B*100, 0)
        else:
            print(0, 0)
    else:
        print(ans_water+ans_suger, ans_suger)


if __name__ == '__main__':
    main()