def main():
    N=int(input())
    S=input()
    p=int(len(S)/2)
    if len(S) % 2 == 0:
        if S[0:p] == S[p:]:
            print('Yes')
            return
        else:
            print('No')
            return
    else:
        print('No')
        return
main()