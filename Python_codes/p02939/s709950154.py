S = list(input())
A = [S[0]]
prev = ""
for x in S[1:]:
    if prev != "":
        A.append(prev + x)
        prev = ""
    elif A[-1] == x:
        prev = x
    else:
        A.append(x)
print(len(A))
