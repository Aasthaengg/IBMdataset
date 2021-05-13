n = int(input().strip())
A = list(map(int, input().strip().split(" ")))

def solver(_sign):
    s = A[0]
    count = 0

    if _sign:
        if s <= 0: # head is positive
            count += abs(s) + 1
            s = 1
    else:
        if s >= 0: # head is negative
            count += abs(s) + 1
            s = -1

    for a in A[1:]:
        prev = s
        sign = prev > 0
        s += a
        if s == 0:
            count += 1
            if sign: # previous is positive
                s = -1
            else: # prev is negative
                s = 1
        elif sign == (s > 0): # previous and current have the same sign
            count += abs(s)+1
            if s > 0:
                s = -1
            else:
                s = 1
        else:
            pass
    return count

print(min(solver(True), solver(False)))