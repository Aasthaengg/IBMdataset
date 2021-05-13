def main():
    X = input()
    result = len(X)
    from collections import deque
    d = deque([])
    append = d.appendleft
    pop = d.popleft
    for x in X:
        if x == "S":
            append(x)
        else:
            if len(d) > 0 and d[0] == "S":
                result -= 2
                pop()
            else:
                append(x)
    print(result)
main()