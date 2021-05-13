import sys
def input(): return sys.stdin.readline().strip()

def main():
    S = input()
    if int(S[5:7]) <= 4: print("Heisei")
    else: print("TBD")



if __name__ == "__main__":
    main()
