import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
    s = input()
    ans = float('inf')
    for i in range(len(s)-2):
        if i == len(s)-3:
            ans = min(ans, abs(int(s[i:]) - 753))
        else:
            ans = min(ans, abs(int(s[i:i+3]) - 753))
    print(ans)
            
if __name__ == '__main__':
    main()