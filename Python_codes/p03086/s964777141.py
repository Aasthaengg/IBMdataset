def main():
    S = str(input())
    longest = 0
    if len(S) < 2:
        if S == 'A' or S == 'G' or S == 'C' or S == 'T':
            print(1)
            return
        else:
            print(0)
            return
    for i in range(len(S)):
        cnt = 0
        loop = 0
        t = 0
        while cnt == 0 and loop + i < len(S):
            if S[loop + i] == 'A' or S[loop + i] == 'G' or S[loop + i] == 'C' or S[loop + i] == 'T':
                t += 1
                if longest < t:
                    longest = t
                loop += 1
            else:
                cnt = 1
    print(longest)
main()