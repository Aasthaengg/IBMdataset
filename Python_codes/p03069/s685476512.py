import sys
#input = sys.stdin.buffer.readline

def main():
    N = int(input())
    s = input()
    ans = s.count(".")
    count = ans
    for st in s:
        if st == "#":
            count += 1
        else:
            count -= 1
        ans = min(ans,count)
        
    print(ans)

if __name__ == "__main__":
    main()