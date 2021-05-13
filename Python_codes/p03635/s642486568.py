from sys import stdin, stdout


def main():
    line = stdin.readline()
    parts = line.split()
    a = int(parts[0])
    b = int(parts[1])

    rta = (a-1)*(b-1)
    stdout.write(str(rta))


main()