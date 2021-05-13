def main():
    h, w, a, b = map(int, input().split())
    s = [[] for _ in [0] * h]
    for i in range(b):
        s[i] = "0" * a + "1" * (w - a)
    for i in range(b, h):
        s[i] = "1" * a + "0" * (w - a)
    for i in s:
        print(i)
main()