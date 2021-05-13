N = int(input())

a = set([])
for i in range(N):
    S = input()
    if S[0] == "i":
        a.add(S[7:])
        #print("a",a)
    else:
        print("yes" if S[5:] in a else "no")

