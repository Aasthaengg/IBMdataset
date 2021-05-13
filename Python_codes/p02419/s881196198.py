def main():
    W = input()
    T = list(linein())

    w = W.lower()
    ans = 0
    for t in T:
        for word in t.split():
            if w == word.lower():
                ans += 1

    print(ans)

def linein():
    while True:
        try:
            s = input()
            if s == 'END_OF_TEXT':
                break
            yield ''.join(s)
        except EOFError:
            break

main()