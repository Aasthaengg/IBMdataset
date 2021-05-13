w = input()
N = int(input())
for n in range(N):
    o = input().split()
    if o[0] == "print":
        print(w[int(o[1]):int(o[2])+1])
    if o[0] == "reverse":
        a = w[int(o[1]):int(o[2])+1]
        w = w[:int(o[1])] + a[::-1] + w[int(o[2])+1:]
    if o[0] == "replace":
        b = [x for x in w]
        i = [y for y in o[3]]
        for j in range(len(i)):
            b[int(o[1])+j] = i[j]
        w = "".join(map(str,b))
            
