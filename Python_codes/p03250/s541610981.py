def main():
    l = [int(i) for i in input().split()]
    l.sort(reverse=True)
    print(10*l[0]+l[1]+l[2])
main()