s = input()
k = int(input())

if k == 1:
    print(s[0])
else:
    count = 0
    for i, v in enumerate(s, 1):
        if v == '1':
            count += 1
        else:
            tmp = v
            break

    if count >= k or count ==len(s) :
        print(1)
    else:
        print(tmp)