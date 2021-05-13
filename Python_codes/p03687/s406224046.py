import sys

sys.setrecursionlimit(10**6)

def handling(string, letter):
    global cnt
    cnt += 1; nxt = []
    for i in range(len(string)-1):
        s1, s2 = string[i], string[i+1]
        if s1 == letter:
            nxt.append(s1)
        elif s2 == letter:
            nxt.append(s2)
        else:
            nxt.append(s1)
    if len(set(nxt)) != 1:
        handling(nxt, letter)

def main():
    global cnt
    s = list(input())
    sletter = set(s)
    if len(sletter) == 1:
        print(0)
        return
    ans = 101
    for l in sletter:
        cnt = 0
        t = s.copy()
        handling(t, l)
        ans = min(ans, cnt)
    print(ans)

if __name__ == "__main__":
    main()
