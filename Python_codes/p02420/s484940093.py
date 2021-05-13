while True:
    n = list(input())
    if n == list("-"):
        break
    m = int(input())
    for i in range(m):
        h = int(input())
        t = n[:h]
        del n[:h]
        n.append(t)
        n = [n for x in n for n in x]
    n = "".join(n)
    print(n)