# B - Magic 2


def magic(a, b, c, k):
    for i in range(k):
        if a >= b:
            b = b * 2
        elif b >= c:
            c = c * 2
        i += 1
    if a < b and b < c:
        return "Yes"
    else:
        return "No"


if __name__ == "__main__":
    param_a, param_b, param_c = map(int, input().split(' '))
    param_k = int(input())
    print(magic(param_a, param_b, param_c, param_k))
