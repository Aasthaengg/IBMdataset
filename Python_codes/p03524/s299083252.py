import sys
input = sys.stdin.readline
def main():
    S = list(input().rstrip())
    A, B, C = 0, 0, 0
    for s in S:
        if s == 'a':
            A += 1
        if s == 'b':
            B += 1
        if s == 'c':
            C += 1
    if len(S) == 1:
        print("YES")
    elif abs(A-B) <= 1 and abs(B-C) <= 1 and abs(C-A) <= 1:
        print("YES")
    else:
        print('NO')

if __name__ == '__main__':
    main()