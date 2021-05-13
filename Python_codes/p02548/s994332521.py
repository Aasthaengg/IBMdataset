def c_a_times_b_plus_c():
    N = int(input())
    return sum((N - 1) // a for a in range(1, N))

print(c_a_times_b_plus_c())