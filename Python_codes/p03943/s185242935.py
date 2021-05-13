
def resolve():
    bags = list(map(int, input().split()))
    print("Yes" if max(bags)*2 == sum(bags) else "No")
    


if '__main__' == __name__:
    resolve()