import sys

def main():
    for line in iter(sys.stdin.readline, ""):
        a = line.rstrip("\n").split(" ")
        b = []
        b.append(int(a[0]))
        b.append(int(a[1]))
        if (b[0] == 0 and b[1] == 0):
            return

        print(str(min(b)) + " " + str(max(b)))
     
if __name__ == "__main__":
    main()