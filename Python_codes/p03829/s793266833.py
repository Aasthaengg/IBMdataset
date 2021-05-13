def main():
    n, a, b = list(map(int, input().split()))
    x = list(map(int, input().split()))
    quantty = 0
    # ans = []
    for i in range(len(x)):
        if i == len(x) - 1:
            break
        quantty += min(a*(x[i+1] - x[i]), b)
        # ans.append(quantty)
    print(quantty)



if __name__ == '__main__':
    main()