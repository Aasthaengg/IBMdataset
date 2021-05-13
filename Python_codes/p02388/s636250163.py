import sys

def main():
    for line in iter(sys.stdin.readline, ""):
        a = line.rstrip("\n")
        b = int(a)
        print (b**3)
     
if __name__ == "__main__":
    main()