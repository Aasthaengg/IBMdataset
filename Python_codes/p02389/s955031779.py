import sys

def main():
    for line in iter(sys.stdin.readline, ""):
        a = line.rstrip("\n").split(" ")
        b = int(a[0])
        c = int(a[1])
        print (str(b*c) + " " + str(2*b+2*c))
     
if __name__ == "__main__":
    main()