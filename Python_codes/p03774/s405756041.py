import sys
def input(): return sys.stdin.readline().strip()

def main():
    N, M = map(int, input().split())
    student = []
    for _ in range(N):
        a, b = map(int, input().split())
        student.append((a, b))
    checkpoint = []
    for _ in range(M):
        c, d = map(int, input().split())
        checkpoint.append((c, d))

    for a, b in student:
        point, dist = -1, 10**18
        for i in range(M):
            c, d = checkpoint[i]
            if abs(a - c) + abs(b - d) < dist:
                point = i
                dist = abs(a - c) + abs(b - d)
        print(point + 1)



if __name__ == "__main__":
    main()
