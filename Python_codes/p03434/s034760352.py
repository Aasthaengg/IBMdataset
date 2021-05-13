def main():
    N = int(input())
    l = [int(x) for x in input().split()]
    Alice = 0
    Bob = 0
    l.sort()
    l.reverse()
    for i in range(len(l)):
        if i % 2 == 0:
            Alice += l[i]
        else:
            Bob += l[i]
    print(Alice-Bob)
main()