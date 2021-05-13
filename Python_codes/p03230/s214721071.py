import math


def main():
    N = int(input())
    x = math.floor(math.sqrt(N*2))
    if x * (x+1) != N*2:
        print("No")
        return
    print("Yes")
    print(x+1)
    s = [[] for _ in range(x+1)]
    counter = 1
    for i in range(x+1):
        for j in range(i+1, x+1):
            s[i].append(counter)
            s[j].append(counter)
            counter += 1
    for i in range(x+1):
        print(len(s[i]), *s[i])


if __name__ == "__main__":
    main()
