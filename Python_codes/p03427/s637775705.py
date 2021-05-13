n = int(input())
d = len(str(n))
n_sum = 0
for i in range(d):
    n_sum += int(str(n)[i])
def judge(n):
    for i in range(1, len(n)):
        if n[i] != "9":
            return True
    return False
print(n // (10 ** (d - 1)) - 1 + 9 * (d - 1) if judge(str(n))  else n_sum)