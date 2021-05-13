N = int(input())

N_1 = round(N/1.08//1)
N_2 = N_1 + 1


if N_1*1.08//1 == N:
    print(N_1)

elif N_2 * 1.08//1 == N:
    print(N_2)

else:
    print(":(")