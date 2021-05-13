s = input()
k = int(input())

if s[0] != "1":
    print(s[0])
    exit()
else:
    cnt = 0
    not_1 = 0
    for i in range(len(s)):
        if s[i] == "1":
            cnt += 1
        else:
            not_1 = i
            break
    if cnt >= k:
        print(1)
        exit()
    else:
        print(s[not_1])