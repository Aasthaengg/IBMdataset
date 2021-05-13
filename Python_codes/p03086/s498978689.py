import sys
input=sys.stdin.readline

def main():
    s = input()
    len_s = len(s)
    cnt = 0
    for i in range(len_s):
        trial = 0
        for k in range(i,len_s):
            if s[k] in "ACGT":
                trial += 1
            else:
                cnt = max(cnt,trial)
                break
    print(cnt)

if __name__=="__main__":
    main()
