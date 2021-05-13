def main():
    s = list(input())
    if s[0] == s[1] == s[2] == s[3]:
        print('No')
        return
    for i in range(3):
        if s[3] == s[i]:
            s.pop(3)
            s.pop(i)
            if s[0] == s[1]:
                print('Yes')
                return
            print('No')
            return
    print('No')
            
main()