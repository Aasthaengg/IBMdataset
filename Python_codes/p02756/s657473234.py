S = list(input())
Q = int(input())
QL = []

for _ in range(Q):
    QL.append(input())

inversed = False
invc = 0

prefix = []
suffix = []

for query in reversed(QL):
    # print("qi:", query)
    if query == '1':
        #1
        inversed = not inversed
        invc += 1
    
    else:
        # print("2:inv:", inversed)
        #2
        __, f, c = query.split()

        if f == '1':
            if inversed:
                suffix.append(c)
            else:
                prefix.append(c)
        else:
            if not inversed:
                suffix.append(c)
            else:
                prefix.append(c)

# print("prefix:", prefix)
# print("suffix:", suffix)

if inversed:
    S = list(reversed(S))

print("".join(prefix) + "".join(S) + "".join(list(reversed(suffix))))