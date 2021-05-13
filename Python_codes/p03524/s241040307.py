S = input()
temp = ["a", "b", "c"]
abc = [S.count(x) for x in temp]
abc.sort(reverse=True)
if abc.count(0) == 1:
    if len(S) == 2:
        print("YES")
    else:
        print("NO")
elif abc.count(0) == 2:
    if len(S) == 1:
        print("YES")
    else:
        print("NO")
elif abc[0] == abc[1] == abc[2]:
    print("YES")
elif abc[0] == abc[1] == abc[2]+1:
    print("YES")
elif abc[0] == abc[1]+1 == abc[2]+1:
    print("YES")
else:
    print("NO")