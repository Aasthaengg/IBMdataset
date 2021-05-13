import re

def main():
    s = input().replace("?", ".")
    t = input()
    ans = []

    for i in range(len(s)-len(t)+1):
        if not re.match(s[i:i+len(t)], t):
            continue
        tmp = (s[:i] + t + s[i+len(t):]).replace(".", "a")
        ans.append(tmp)

    if not ans:
        print("UNRESTORABLE")
    else:
        print(min(ans))

if __name__ == "__main__":
    main()