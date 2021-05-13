def main():
    s = input()
    count = 0
    b_count = []
    for v in s:
        if v == "B":
            count += 1
        if v == "W":
            b_count.append(count)
    print(sum(b_count))

def input_list():
    return map(int, input().split())

if __name__ == "__main__":
    main()