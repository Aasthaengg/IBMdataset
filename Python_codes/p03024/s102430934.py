S = str(input())
count = S.count("o")
if (count-len(S)) >= -7:
    print("YES")
else:
    print("NO")
