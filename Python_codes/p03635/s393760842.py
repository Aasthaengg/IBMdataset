from sys import stdin, stdout


def main():
    line = stdin.readline()
    parts = line.split()
    n = int(parts[0])
    m = int(parts[1])
    stdout.write(str((n-1)*(m-1)))


main()
