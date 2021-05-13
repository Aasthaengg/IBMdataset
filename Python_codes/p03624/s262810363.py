import sys
def input(): return sys.stdin.readline().strip()

def main():
    S = input()
    d = set()
    for c in S: d.add(c)
    for i in range(26):
        if chr(i + 97) not in d:
            print(chr(i + 97))
            return
    print("None")
    
    


if __name__ == "__main__":
    main()
