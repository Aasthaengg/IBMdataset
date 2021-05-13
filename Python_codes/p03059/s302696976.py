def main():
    s, b, e = [int(x) for x in input().split()]
    e += 0.5
    levas = e // s
    print(int(levas*b))
main()