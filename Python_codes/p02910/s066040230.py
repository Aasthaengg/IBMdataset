def resolve():
    S = input()
    for i, c in enumerate(list(S)):
        if i%2==0:
            if c == "L":
                print("No")
                return
        else:
            if c == "R":
                print("No")
                return
    print("Yes")

if '__main__' == __name__:
    resolve()