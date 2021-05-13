
KEY = "keyence"

def main():
    s = input()

    if s.startswith(KEY) or s.endswith(KEY):
        print("YES")
        return

    for i in range(1, len(KEY)):
        st = KEY[0:i]
        ed = KEY[i:]

        if s.startswith(st) and s.endswith(ed):
            print("YES")
            return

    print("NO")

main()
