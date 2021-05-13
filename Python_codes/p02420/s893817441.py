while True:
    string = list(input())
    if len(string) == 1 and string[0] == "-":
        break
    num = int(input())
    for i in range(num):
        times = int(input())
        tmp = string[:times]
        del string[:times]
        string += tmp
    print("".join(string))