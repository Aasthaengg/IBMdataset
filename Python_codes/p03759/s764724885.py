def main(a, b, c):
    A = int(a) - int(b)
    B = int(b) - int(c)
    if A == B:
        print("YES")
    else:
        print("NO")

[a, b, c] = input().split()
main(a, b, c)
