def main():
    S = input()
    flag = True
    cnt = 0
    for i in range(len(S)):
        if i == 0:
            if S[i] != 'A':
                print("WA")
                return
        else:
            if 2 <= i <= len(S)-2 and S[i] == 'C':
                cnt += 1
            elif S[i].isupper():
                print("WA")
                return
    if cnt == 1:
        print("AC")
    else:
        print("WA")
            
main()