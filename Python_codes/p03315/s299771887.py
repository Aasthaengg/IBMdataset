def main():
    S = list(str(input()))
    count = 0
    for i in S:
        if i == '+':
            count += 1
        else:
            count -= 1
    print(count)
main()