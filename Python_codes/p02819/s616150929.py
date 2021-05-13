def main():
    x = int(input())
    for i in range(x, 110000):
        count = 0
        for j in range(1, i+1):
            if i % j == 0: count += 1
            if count > 3: continue
        if count == 2: return i


print(main())