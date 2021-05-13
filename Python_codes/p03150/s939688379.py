S = input()

key = list("keyence")
target = 'keyence'

flg = False
for i in range(len(S)):
    for j in range(len(S)):
        tmp = S[0:i]+S[j:]

        if tmp == target and not flg:
            print("YES")
            flg = True
            break

if not flg:
    print("NO")
