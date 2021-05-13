if __name__ == "__main__":
    N = input()
    n_list = []

    for n in N:
        n_list.append(int(n))

    n_sum = sum(n_list)

    ans = 'Yes' if n_sum % 9 == 0 else 'No'

    print(ans)