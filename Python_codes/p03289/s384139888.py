def main():
    S = str(input())
    cnt = 0
    if S[0] == 'A':
        for i in range(2, len(S)-1):
            if S[i] == 'C':
                cnt += 1
        if cnt == 1:
            for i in range(1, len(S)):
                if S[i] == 'C':
                    continue
                elif S[i].islower():
                    continue
                else:
                    print('WA')
                    return
        else:
            print('WA')
            return
    else:
        print('WA')
        return
    print('AC')
    
main()  