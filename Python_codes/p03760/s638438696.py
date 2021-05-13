import sys
def input(): return sys.stdin.readline().strip()

def main():
    O = input()
    E = input()
    password = ""
    for o, e in zip(O, E):
        password += o + e
    if len(O) > len(E): password += O[-1]
    print(password)
    

if __name__ == "__main__":
    main()
