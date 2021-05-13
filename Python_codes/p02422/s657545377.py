from sys import stdin

s = stdin.readline().rstrip()
q = int(stdin.readline().rstrip())
for i in range(q):
    query = stdin.readline().rstrip().split()
    query[1] = int(query[1])
    query[2] = int(query[2])

    if query[0] == "print":
        print(s[query[1]:query[2]+1])
    elif query[0] == "reverse":
        s = s[:query[1]] + s[query[1]:query[2]+1][::-1] + s[query[2]+1:]
    elif query[0] == "replace":
        s = s[:query[1]] + query[3] + s[query[2]+1:]
