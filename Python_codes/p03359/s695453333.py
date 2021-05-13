from sys import stdin, stdout

def main():
    line = stdin.readline()
    parts = line.split()
    mes = int(parts[0])
    dia = int(parts[1])

    stdout.write(str(mes if dia>=mes else mes-1))

main()