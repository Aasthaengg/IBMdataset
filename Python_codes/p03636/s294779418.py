from sys import stdin
def main():
    readline=stdin.readline
    S=readline().strip()
    print(S[0]+str(len(S)-2)+S[-1])
if __name__=="__main__":
    main()