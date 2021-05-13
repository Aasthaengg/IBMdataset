n = int(input())

def sum_seq(d):
    return 0.5*(n//d)*(2*d+(n//d-1)*d)

print(int(sum_seq(1) - sum_seq(3) - sum_seq(5) + sum_seq(15)))
