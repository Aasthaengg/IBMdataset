def main():
    K = int(input())
    op = K//50
    ans = [i+op for i in range(50)]
    op_d = K % 50
    for i in range(op_d):
        for j in range(50):
            if i == j:
                ans[j] += 50
            else:
                ans[j] -= 1
    print(50)
    print(*ans)


if __name__ == '__main__':
    main()
