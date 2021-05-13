import sys
#input = sys.stdin.buffer.readline

def main():
    N = int(input())
    AB = [0,0,0]
    ans = 0
    for _ in range(N):
        s = input()
        l = len(s)
        if s[0] == "B" and s[-1] == "A":
            AB[2] += 1
        else:
            if s[0] == "B":
                AB[1] += 1
            if s[-1] == "A":
                AB[0] += 1
        for i in range(l-1):
            if s[i] == "A" and s[i+1] == "B":
                ans += 1

    if (AB[0]+AB[1] == 0 and AB[2] != 0):
        print(ans+AB[2]-1)
    else:
        print(ans+min(AB[0],AB[1])+AB[2])
    
if __name__ == "__main__":
    main()