from sys import stdin

def main():
    n = stdin.readline()
    if(n[0] == n[1] and n[1] == n[2]):
        print("Yes")
    elif(n[1] == n[2] and n[2] == n[3]):
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()