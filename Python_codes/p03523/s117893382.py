def main():

    S = input()
    T = "AKIHABARA"

    cur = set([""])
    for i in range(len(T)):
        temp = set()
        for s in cur:
            temp.add(s + T[i])
            if T[i] == "A":
                temp.add(s)
        cur = temp
    if S in cur:
        return "YES"
    return "NO"


if __name__ == '__main__':
    print(main())