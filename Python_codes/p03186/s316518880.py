def main30():
    A, B, C = (int(x) for x in input().split())

    count = 0

    if (C-B) <= A:
        print(B+C)
    else:
        print(A+2*B+1)

main30()