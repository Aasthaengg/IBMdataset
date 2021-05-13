def deco_fibo(func):
    answer_list = [1, 1] + [None] * 43
    def main_fibo(i):
        ans = answer_list[i]
        if ans:
            return ans
        ans = func(i)
        answer_list[i] = ans
        return ans
    return main_fibo

@deco_fibo
def fibo(num):
    return fibo(num - 1) + fibo(num - 2)


n = int(input())

print(fibo(n))