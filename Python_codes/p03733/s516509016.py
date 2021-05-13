def main():
    IN1 = [int(_) for _ in input().split()]
    N = IN1[0]
    T = IN1[1]
    times = [int(_) for _ in input().split()]

    result = 0
    before = 0
    base = 0 
    for i in range(1, len(times)):
        time = times[i]
        if time - before > T:
            result = result + before + T - base
            base = time
        before = time
    result = result + times[len(times)-1] + T - base
    print(result)

if __name__ == "__main__":
    main()