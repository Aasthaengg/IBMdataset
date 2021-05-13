import sys
def input(): return sys.stdin.readline().strip()

def main():
    s1, s2, s3 = input().split()
    print(str.upper(s1[0]) + str.upper(s2[0]) + str.upper(s3[0]))
    

if __name__ == "__main__":
    main()
