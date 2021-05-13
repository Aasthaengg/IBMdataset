def main():
    import sys
    input = sys.stdin.readline
    N, A, B, C, D = [int(x) for x in input().strip().split()]
    A, B, C, D = A-1, B-1, C-1, D-1
    S = input().strip()
    if C == D:
        print('No')
        return
    if C > D:
        C, D = D, C
        A, B = B, A
    while B != D:
        # print(S)
        # print(' ' * A + 'A')
        # print(' ' * B + 'B')
        if B + 2 < N and B + 2 != A and S[B+2] == '.':
            B += 2
        elif B + 1!= A and S[B+1] == '.':
            B += 1
        else:
            if A > B:
                if A + 1 < N and B != A + 1 and S[A+1] == '.':
                    A += 1
                elif A + 2 < N and B != A + 2 and S[A+2] == '.':
                    A += 2
                else:
                    print('No')
                    return
            else:
                print('No')
                return
    
        
    while A != C:
        # print(S)
        # print(' ' * A + 'A')
        # print(' ' * B + 'B')
        if A + 2 < N and B != A + 2 and S[A+2] == '.':
            A += 2
        elif A + 1 < N and B != A + 1 and S[A+1] == '.':
            A += 1
        else:
            print('No')
            return

    # print(S)
    # print(' ' * A + 'A')
    # print(' ' * B + 'B')
    print('Yes')



if __name__ == '__main__':
    main()