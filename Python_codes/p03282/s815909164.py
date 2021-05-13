import sys

input = sys.stdin.readline

def main():
    ans = ''
    index = 0
    s = input().rstrip('\n')
    k = int(input())
    for i in range(len(s)):
        if s[i] != '1':
            ans = s[i]
            index = i
            break
    if ans == '' or k < index+1:
        ans = '1'
    print(ans)

if __name__ == '__main__':
    main()