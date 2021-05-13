from sys import stdin,stdout

def main():
    line=stdin.readline()
    parts=line.split()
    a=int(parts[0])
    par=int(a/2)
    impar=int(a/2)+a%2
    stdout.write(str(par*impar))
main()