S = list(input())
if len([x for x in set(S) if S.count(x) > 1]) == 0:
    print("yes")
else:
    print("no")
