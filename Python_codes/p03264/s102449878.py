from sys import stdin, stdout


def main():
    line = stdin.readline()
    parts = line.split()
    a = int(parts[0])

    even = int(a/2)
    odd = a - even
    rta = even * odd
    stdout.write(str(rta))


main()