def main():
    a, b = map(int, input().split())
    A = 0
    B = 1
    for i in range(1, 1000):
        A += i
        B += i + 1 
        if b - a == B - A:
            print(A - a) 
main()  