A, B, C = map(int, input().split())
def check():
    if abs(B-A)<abs(C-A):
        return 'A'
    return 'B'
print(check())