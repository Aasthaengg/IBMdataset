def operation(s,t):
    cnt = 0
    if s == t:
        return cnt
    for i in range(len(s)):
        if s[i]!=t[i]:
            cnt+=1
    return cnt

def main():
    s = str(input())
    t = str(input())
    print(operation(s,t))

if __name__ == '__main__':
    main()