
def resolve():
    n = int(input())
    s = input()
    t = input()
    ans = len(s) + len(t)
    for i in range(len(s)):
        pos = 0
        for ss,tt in zip(s[i:],t):
            if ss != tt:
                break
            pos += 1
        else:
            if len(s) - i > len(t) or i + len(t) < n:
                continue
            tmp = i + len(t)
            if tmp < ans:
                ans = tmp
    print(ans)
        

if __name__ == "__main__":
    resolve()
