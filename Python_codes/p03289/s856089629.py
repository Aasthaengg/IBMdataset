import re

def solve():
    S = input()
    print('AC' if re.match(r'^A[a-z]+C[a-z]+$', S) else 'WA')

if __name__ == "__main__":
    solve()