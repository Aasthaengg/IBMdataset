from sys import stdin, stdout


def main():
    line = stdin.readline()
    parts = line.split()
    a = int(parts[0])
    b = int(parts[1])

    if a <= b:
        stdout.write(str(a))
    else:
        stdout.write(str(a - 1))


main()