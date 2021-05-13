def main():
    S = input()

    for i in range(len(S)):
        for j in range(len(S)):
            if 'keyence' == S[:i] + S[j:]:
                print('YES')
                return

    print('NO')
    
main()