def factorization(n):
    factorization_list = [1]
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp % i == 0:
            count = 0
            while temp % i == 0:
                count += 1
                temp //= i
            factorization_list.append(i)

    if temp != 1:
        factorization_list.append(temp)

    if factorization_list==[]:
        factorization_list.append(n)

    return factorization_list


if __name__ == "__main__":
    A, B = map(int, input().split())
    A_fac = set(factorization(A))
    B_fac = set(factorization(B))

    AB_fac = A_fac & B_fac
    print(len(AB_fac))