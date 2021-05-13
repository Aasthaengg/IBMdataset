from collections import defaultdict

def main():
    W,H,N = [int(x) for x in input().split()]
    x1,y1 = 0,0
    x2,y2 = W,H
    x3,y3 = 0,0
    x4,y4 = W,H
    A = defaultdict(list)
    for _ in range(N):
        x,y,a = [int(x) for x in input().split()]
        A[a].append((x,y))
    if A[1]:
        x1,y1 = max(A[1], key=(lambda x: x[0]))
    if A[2]:
        x2,y2 = min(A[2], key=(lambda x: x[0]))
    if A[3]:
        x3,y3 = max(A[3], key=(lambda x: x[1]))
    if A[4]:
        x4,y4 = min(A[4], key=(lambda x: x[1]))
    if x1 >= x2 or y3 >= y4:
        print(0)
    else:
        print((x2-x1)*(y4-y3))

if __name__ == '__main__':
    main()