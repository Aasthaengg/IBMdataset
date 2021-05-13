# Panasonic2020 D - String Equivalence
def generator(n):
    if n == 1:
        yield [0]
    else:
        for A in generator(n - 1):
            for i in range(max(A) + 2):
                A.append(i)
                yield A
                A.pop()


n = int(input())
for A in generator(n):
    s = ''
    for a in A:
        s += chr(a + 97)
    print(s)
