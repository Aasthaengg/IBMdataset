def resolve():
    from collections import deque
    x = input()
    final = deque([])
    final.append(x[0])
    for i in range(1, len(x)):
        if x[i] == "S":
            final.append("S")
        else:
            if not final:
                final.append("T")
            else:
                last = final.pop()
                if last == "S":
                    continue
                else:
                    final.append("T")
                    final.append("T")
    print(len(final))
resolve()