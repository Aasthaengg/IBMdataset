import sys
S = input()
if len(S)<26:
    for i in range(26):
        ans = S + chr(97+i)
        if len(ans) == len(list(set(ans))):
            print(ans)
            break
else:
    if S == 'zyxwvutsrqponmlkjihgfedcba':
        print(-1)
    else:
        SS = S[0:-1]
        while True:
            SS = SS[0:-1]
            for i in range(26):
                ans = SS + chr(97+i)
                if len(ans) == len(list(set(ans))) and S < ans:
                    print(ans)
                    sys.exit()