S = input().rstrip()
Q = int(input().rstrip())
a = -1
before =[]
after =[]
for _ in range(Q):
    stdin = input().rstrip()
    if int(stdin[0]) == 1:
        a = ~a
    else:
        T,F,C = stdin.split()
        if int(F) == 2+a:
            before.append(C)
        else:
            after.append(C)
S = ''.join(before)[::-1] + S + ''.join(after)
if a == 0:
    S = S[::-1]
print(S)