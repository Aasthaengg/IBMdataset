n = int(input())
a = list(map(int, input().split()))

if n == 3:
    if a[0] == a[1]^a[2]:
        print("Yes")
    else:
        print("No")
elif sum(a) == 0:
    print("Yes")
else:
    vals = []
    cnts = []

    for i in range(n):
        if a[i] in vals:
            cnts[vals.index(a[i])] += 1
        else:
            if len(vals) == 3:
                print("No")
                exit()

            vals.append(a[i])
            cnts.append(1)

    if len(vals) == 3 and (vals[0] == vals[1]^vals[2]) and (cnts[0] == cnts[1] and cnts[1] == cnts[2]):
        print("Yes")
    elif len(vals) == 2 and (vals[0] == 0 or vals[1] == 0):
        if vals[0] == 0 and  2*cnts[0] == cnts[1]:
            print("Yes")
        elif vals[1] == 0 and cnts[0] == 2*cnts[1]:
            print("Yes")
        else:
            print("No")
    else:
        print("No")