import sys
input = lambda: sys.stdin.readline().rstrip()
input_nums = lambda: list(map(int, input().split()))

def main():
    b = input()
    at = ('A', 'T')
    cg = ('C', 'G')
    revAT = lambda x: at[0] if x != 'A' else at[1]
    revCG = lambda x: cg[0] if x != 'C' else cg[1]
    if b == 'A' or b == 'T': print(revAT(b))
    else: print(revCG(b))

if __name__ == '__main__':
    main()
