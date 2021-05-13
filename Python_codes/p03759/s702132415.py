
def resolve():
    a, b, c = list(map( int, input().split() ))
    print("YES" if b-a == c-b else "NO")
    


if '__main__' == __name__:
    resolve()