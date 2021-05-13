s = input()
k = int(input())

if len(s) == 1:
    print(s)
    exit()

if s[0] == "1":
    if k == 1:
        print(1)
        exit()
    else:
        for i in range(len(s)):
            if s[i] == "1":
                continue
            elif (s[i] != "1") and (i+1 <= k):
                print(s[i])
                exit()
            elif (s[i] != "1") and (i+1 > k):
                print(1)
                exit()
        print(1)
        exit()

elif s[0] != "1":
    print(s[0])
    exit()
