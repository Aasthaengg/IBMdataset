import sys
input=sys.stdin.readline

def main():
    s = input()
    cnt = 0
    trial = 0
    for i in s: # 本当に全通りO（n^2）やらなくても最長の部分がわかれば良い
        if i in "ACGT":
            trial += 1
        else:
            cnt = max(cnt, trial)
            trial = 0
    print(cnt)

if __name__=="__main__":
    main()
