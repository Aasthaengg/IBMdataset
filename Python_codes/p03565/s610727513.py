import sys
MOD = 10**9 + 7
# import io, os
# input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline
def input():
    return sys.stdin.readline()[:-1]

def main():
    s = input()
    t = input()
    for k in range(len(s)-len(t),-1,-1):
        f = 1
        for i in range(len(t)):
            if s[k+i] != "?":
                if s[k+i] != t[i]:
                    f = 0
                    break
        if f == 1:
            print(s[:k].replace("?","a") + t + s[k+len(t):].replace("?","a"))
            exit()
    print("UNRESTORABLE")
if __name__ == '__main__':
    main()
