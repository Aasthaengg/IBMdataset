def main():
    a, b = map(int, input().split())
    A = ''
    for i in range(b):
        A = str(a) + A
    B = ''
    for i in range(a):
        B = str(b) + B
    dicA = int(A[0])
    dicB = int(B[0])
    if dicA < dicB:
        print(A)
    else:
        print(B)
main()