def main():
    N = int(input())

    idx = 0
    for i in range(1, 5000):
        if i*(i+1)//2 <= N:
            idx = i

    delta = N - idx * (idx + 1) // 2

    r = m = 0
    if delta % idx == 0 and delta != 0:
        r = 1
    else:
        r, m = divmod(delta, idx)

    prob = [r + (i + 1) for i in range(idx)]

    for i in range(1, m + 1):
        prob[idx - i] += 1

    for i in range(len(prob)):
        print(prob[i])

if __name__ == "__main__":
    main()