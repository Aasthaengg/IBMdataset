def main():
    A, B, C = map(int, input().split())
    l = [A, B, C]
    l.sort()
    if l[0] == l[1]:
        print(l[2])
    elif l[0] == l[2]:
        print(l[1])
    else:
        print(l[0])
main()