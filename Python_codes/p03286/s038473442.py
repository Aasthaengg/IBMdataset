def negaternary(i: int) -> str:

    if i == 0:
        digits = ['0']
    else:
        digits = []
        while i != 0:
            i, remainder = divmod(i, -2)
            if remainder < 0:
                i, remainder = i + 1, remainder + 2
            digits.append(str(remainder))
    return ''.join(digits[::-1])

n=int(input())
print(negaternary(n))