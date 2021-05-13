def main():
    N = int(input())
    P = []
    M = []
    for i in range(N):
        s = input()
        left = 0
        right = 0
        rightmax = 0
        for c in s:
            if c == "(":
                left += 1
            else:
                right += 1
            rightmax = max(rightmax, right - left)
        leftdiff = left-right
        if leftdiff >= 0:
            P.append((leftdiff, rightmax, 0, s))
            continue
            
        left = 0
        right = 0
        leftmax = 0
        for c in reversed(s):
            if c == "(":
                left += 1
            else:
                right += 1
            leftmax = max(leftmax, left - right)
        M.append((leftdiff, 0, leftmax, s))

    R = []
    for e in sorted(P, key=lambda _e: _e[1]):
        R.append(e[3])
    for e in sorted(M, key=lambda _e: _e[2], reverse=True):
        R.append(e[3])

    nleft = 0
    for c in "".join(R):
        if c == "(":
            nleft += 1
        else:
            nleft -= 1
        if nleft < 0:
            print("No")
            return
        
    if nleft == 0:
        print("Yes")
    else:
        print("No")


main()
