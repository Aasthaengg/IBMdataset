def main():
    N = int(input())
    A = [int(_) for _ in input().split()]
    B = [int(_) for _ in input().split()]
    if sum(A) < sum(B):
        print(-1)
        return
    tariruhito = []
    tarinai = 0
    output = 0
    for a, b in zip(A, B):
        if a >= b: tariruhito.append(a-b)
        else:
            output += 1
            tarinai += b - a
    tariruhito.sort(reverse=True)
    i = 0
    while tarinai > 0:
        output += 1
        tarinai = max(0, tarinai-tariruhito[i])
        i += 1
    print(output)
    return

if __name__ == '__main__':
    main()
