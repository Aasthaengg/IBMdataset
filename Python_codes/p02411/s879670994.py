def f(s):
    m, f, r = list(map(int, s.split()))
    if m == -1 or f == -1:
        return "F"

    t = m + f
    if 80 <= t:
        return "A"
    elif 65 <= t:
        return "B"
    elif 50 <= t:
        return "C"
    elif 30 <= t:
        return "C" if 50 <= r else "D"
    else:
        return "F"

while True:
    s = input()
    if s == "-1 -1 -1":
        break
    print(f(s))