import sys

N = int(sys.stdin.readline())

def main():
    print(0)
    sys.stdout.flush()
    r = sys.stdin.readline().strip()
    if r == 'Vacant':
        return
    if r == 'Male':
        t = ['Male', 'Female']
    else:
        t = ['Female', 'Male']
    left = 1
    right = N - 1

    while True:
        pos = (left + right) // 2
        print(pos)
        sys.stdout.flush()
        r = sys.stdin.readline().strip()
        if r == 'Vacant':
            return
        if t[pos % 2] == r:
            left = pos + 1
        else:
            right = pos - 1

main()