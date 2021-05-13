def main():
    S = str(input())
    odd = (len(S) // 2) + (len(S) % 2)
    even = len(S) // 2
    check_odd = 0
    check_even = 0
    c = 0
    for i in range(odd):
        if S[c] == 'R' or S[c] == 'U' or S[c] == 'D':
            check_odd = check_odd + 1
        c = c + 2
    c = 1
    for i in range(even):
        if S[c] == 'L' or S[c] == 'U' or S[c] == 'D':
            check_even = check_even + 1
        c = c + 2
    if check_even == even and check_odd == odd:
        print('Yes')
    else:
        print('No')
main()  