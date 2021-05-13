from sys import stdin, stdout

def main():
    line = stdin.readline()
    parts = line.split()
    par = int(int(parts[0])/2)
    impar = int(int(parts[0])/2) + int(parts[0])%2

    stdout.write(str(par * impar))

main()