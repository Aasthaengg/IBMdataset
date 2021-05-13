
def main():
    n = int(input())
    s = input()
    t = input()

    if s == t:
        print(n)
        return

    for i in reversed(range(0, n)):
        target = s + t[i:]
        if target.startswith(s) and target.endswith(t):
            print(len(target))
            return

main()
