import sys
read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines

def main():
    S = readline().strip()
    N = len(S)

    seq = [1]
    for i in range(N-1):
        if S[i+1] == S[i]:
            seq[-1] += 1
        else:
            seq.append(1)
    
    ans = len(seq) - 1
    print(ans)



if __name__ == "__main__":
    main()
