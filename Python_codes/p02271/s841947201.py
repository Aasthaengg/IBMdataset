import sys

def exhaustiveSearch(A, m, i, s):
    if A[i] == m:
        return True
    elif i == len(A) - 1 or m < 0 or m > s:
        return False

    return exhaustiveSearch(A, m, i + 1, s) or exhaustiveSearch(A, m - A[i], i + 1, s)

if __name__ == "__main__":
    lines = sys.stdin.readlines()
    A = map(int, lines[1].split())
    M = map(int, lines[3].split())
    s = sum(A)

    for m in M:
        if exhaustiveSearch(A, m, 0, s):
            print "yes"
        else:
            print "no"